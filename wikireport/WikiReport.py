# -*- coding: utf-8 -*-

"""Inserts the Trac report into the wiki page."""

name = "WikiReport"
author = "Andrey Rodionov"
revision = "0.1.0"
url = ""
license = "GPL"

from trac.util.translation import _, cleandoc_
from genshi.builder import tag
from trac.wiki.macros import WikiMacroBase
from trac.web.chrome import (INavigationContributor, Chrome,
                             add_ctxtnav, add_link, add_script,
                             add_script_data, add_stylesheet, add_warning,
                             web_context)
from trac.ticket.query  import TicketQueryMacro
from trac.ticket.report import ReportModule
import pkg_resources
import os
import re
import pkg_resources


class WikiReport(WikiMacroBase):
    _description = cleandoc_(
    """Wiki macro inserts the Trac report into the wiki page.
    
    This macro accepts a comma-separated list of keyed parameters,
    in the form "key=value" and "id".
       - "key" -- then report parameter
       - "value" -- then value of report parameter
       - "id" -- then report id of the Trac
    """)
    
    
    def expand_macro(self, formatter, name, args):
        req = formatter.req
        chrome = Chrome(self.env)
        report = ReportModule(self.env)
        
        comma_splitter = re.compile(r'(?<!\\),')
        kwargs = {}
        for arg in comma_splitter.split(args):
            arg = arg.replace(r'\,', ',')
            m = re.match(r'\s*[^=]+=', arg)
            if m:
                kw = arg[:m.end() - 1].strip()
                value = arg[m.end():]
                req.args[kw] = value
            else:
                id = int(arg)
        
        req.args['page'] = '1'
        template, data, content_type = report._render_view(req, id)
        add_stylesheet(req, 'common/css/report.css')
        
        fullpath = ''
        if pkg_resources.resource_exists('wikireport', 'WikiReport.html'):
            fullpath = pkg_resources.resource_filename('wikireport', 'WikiReport.html')
        else:
            filepath = os.path.dirname(os.path.abspath( __file__ ))
            fullpath = os.path.join(filepath, 'WikiReport.html')
    
        return chrome.render_template(req, fullpath, data, None, fragment=True)