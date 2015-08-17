# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

config = {
    'name'                  : 'python-code-demo',
    'description'           : 'A framework for demoing code stuff',
    'long_description'      : (read('README.md') + '\n\n' +
                               read('HISTORY.md')),
    'author'                : 'Wes McNamee',
    'author_email'          : 'ghost.squadron@gmail.com',
    'url'                   : 'https://github.com/ghostsquad/Python-Code-Demo',
    'download_url'          : 'https://github.com/ghostsquad/Python-Code-Demo',
    'version'               : '0.1',
    'install_requires'      : ['pytest', 'achoo', 'mock'],
    'packages'              : find_packages(exclude=['tests*']),
    'include_package_data'  : True,
    'scripts'               : [],
    'py_modules'            : ['pem'],

    #https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'classifiers': [
        'Private :: Do Not Upload',
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
    ],

}
setup(**config, requires=['mock', 'colorama', 'docopt'])
