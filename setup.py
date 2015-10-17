#!/usr/bin/python

from setuptools import setup

setup(
    name = 'WikiReport',
    version = '0.1.0',
    keywords = 'trac macros report',
    author = 'Andrey Rodionov',
    author_email = 'roand@inbox.ru',
    url = '',
    description = 'Wiki macro inserts the Trac report into the wiki page',
    long_description = """
    Wiki macro inserts the Trac report into the wiki page.
    
    This macro accepts a comma-separated list of keyed parameters,
    in the form "key=value" and "id".
       - "key" -- then report parameter
       - "value" -- then value of report parameter
       - "id" -- then report id of the Trac
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
