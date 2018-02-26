#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. module:: pyproject
.. moduleauthor:: Julien Spronck
.. created:: Apr 2015

Simple module to create files and directories in a python project
"""

import pyproject.python_project
import pyproject.flask_project

__version__ = '2.0'

KNOWN_MODULES = ['python', 'flask']


def main():
    '''Main program
    '''
    import six
    import sys

    def usage(exit_status):
        '''
        Displays the usage/help of this script
        '''
        msg = "\npyproject sets up starter files for different types of \n"
        msg += "programming projects.\n\n"
        msg += "\nUsage: \n\n"
        msg += "    pyproject <PROJECT_TYPE> [OPTIONS] ...\n\n"
        msg += "Arguments:\n\n"
        msg += "    PROJECT_TYPE: the type of the project you want to start\n"
        msg += "\n        Available project types:\n"
        msg += "            - python: type `pyproject python -h` for help\n"
        msg += "            - flask: type `pyproject flask -h` for help\n"
        msg += "\nOptions:\n\n"
        msg += "    Available options are specific to each project type\n\n"

        six.print_(msg)
        sys.exit(exit_status)

    import getopt

    # Parse command line options/arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "hv",
                                   ["help", "version"])
    except getopt.GetoptError:
        usage(2)

    for opt, _ in opts:
        if opt in ("-h", "--help"):
            usage(0)
        if opt in ("-v", "--version"):
            six.print_('pyproject {0}'.format(__version__))
            sys.exit()

    if not args:
        usage(2)

    submodule = args[0]

    if submodule not in KNOWN_MODULES:
        usage(3)

    if submodule == 'python':
        pyproject.python_project.main()
    elif submodule == 'flask':
        pyproject.flask_project.main()


if __name__ == '__main__':
    main()
