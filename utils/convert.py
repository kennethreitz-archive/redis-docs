#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
converter
~~~~~~~~~

This module converts the redis documentation to ReSt for further QA.


Dependencies
------------

    Python:
        clint   (http://github.com/kennethreitz/clint)
        pyandoc (http://github.com/kennethreitz/pyandoc)

    Haskell:
        pandoc  (http://johnmacfarlane.net/pandoc/)

Usage
-----

    $ convert.py <redis-html-dir> <output-dir>

"""

import os
import sys


import pandoc

from clint import args
from clint.utils import mkdir_p
from clint.textui import puts, puts_err, colored, indent, progress


USAGE = '$ ./convert.py <redis-html-dir> <output-dir>'



def convert_html_to_rst(html):
    """Returns ReSt version of given HTML"""

    doc = pandoc.Document()
    doc.html = html

    return doc.rst

def scrub_input_paths(paths):

    if not paths:
        return None

    for path in paths:
        if not path.endswith('.html'):
            paths.remove(path)

    return paths


def main():
    """Converter main dispatch."""

    # CLI argument handling.

    input_docs = scrub_input_paths(args.files)
    path_export = args.get(1)

    puts_err(colored.blue('Redis Docs Converter'))

    with indent(2):
        if (input_docs is None) or (path_export is None):
            puts_err('{0} {1}'.format(colored.green('Usage:'), USAGE))
            sys.exit(64)


    with indent(3, quote=' .'):
        puts_err('Converting docs from \'{0}\'.'.format(colored.red(args.get(0))))

        mkdir_p(path_export)
        os.chdir(path_export)

        for path in progress.bar(input_docs, label='   '):

            fname = path.split(os.sep)[-1]
            fname = fname.replace('.html', '.rst')

            with open(path, 'r') as f:
                html = convert_html_to_rst(f.read())

            with open(fname, 'w') as f:
                f.write(html)

        puts('Done!  {0}'.format(colored.yellow(r'\o/')))


if __name__ == '__main__':
    main()