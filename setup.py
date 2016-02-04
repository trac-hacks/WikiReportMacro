#!/usr/bin/python

from setuptools import setup

setup(
    name = 'WikiReport',
    version = '0.2.0',
    keywords = 'trac macros report',
    author = 'Andrey Rodionov',
    author_email = 'roand@inbox.ru',
    url = 'https://github.com/trac-hacks/WikiReportMacro',
    description = 'Wiki macro inserts the Trac report into the wiki page',
    long_description = """
    Wiki macro inserts the Trac report into the wiki page.
    
       [[WikiReport(<id>,<key1>=<value1>, <keyN>=<valueN>, ...)]]
    
    This macro accepts a comma-separated list of keyed parameters,
    in the form "key=value" and "id".
       - "id" -- then report id of the Trac
       - "key" -- then report parameter
       - "value" -- then value of report parameter
    It supports dynamic variables.
    """,
    license = 'GPL',

    install_requires = ['Trac >= 0.12'],

    packages = ['wikireport'],
    package_data = {
        'wikireport': [
            'WikiReport.html',
        ],
    },
    entry_points = {
        'trac.plugins':[
            'wikireport.WikiReport = wikireport.WikiReport',
        ]
    },
)
