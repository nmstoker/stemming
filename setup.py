#!python

import os.path, sys
from setuptools import setup, find_packages

setup(
    name = "stemming",
    version = "1.0.1",
    #package_dir = {'': ''},
    packages = ["stemming"],
    
    author = "Matt Chaput",
    author_email = "matt@whoosh.ca",
    description = "Python implementations of various stemming algorithms.",
    
    long_description = """
This is fork of original public domain repo by Matt Chaput to support Python 3
and move it to Github by Neil Stoker.

Python implementations of the Porter, Porter2, Paice-Husk, and Lovins stemming
algorithms for English. These implementations are straightforward and
efficient, unlike some Python versions of the same algorithms available on the
Web. This package is an extraction of the stemming code included in the Whoosh
search engine.

Note that these are *pure Python* implementations. Python wrappers for, e.g.
the Snoball stemmers and the C implementation of the Porter stemmer are
available on PyPI and will be faster if using compiled code is an option for
you.

Stemming algorithms attempt to automatically remove suffixes (and in some
cases prefixes) in order to find the "root word" or stem of a given word. This
is useful in various natural language processing scenarios, such as search.

In general ``porter2`` is the best overall stemming algorithm, but not
necessarily the fastest or most aggressive.

The ``stemming`` package contains modules for each algorithm (``lovins``,
``paicehusk``, ``porter``, and ``porter2``). Each module contains a ``stem()``
function::

    >> from stemming.porter2 import stem
    >> stem("factionally")
    faction

(The Paice-Husk algorithm allows custom stemming rule sets, so the
``paicehusk`` module also includes a ``PaiceHuskStemmer`` class you can
instantiate with custom rules.)

The original source code for this package is available on BitBucket:

http://bitbucket.org/mchaput/stemming

Please use BitBucket to file bug reports or feature requests:

http://bitbucket.org/mchaput/stemming/issues/
""",

    license = "Public Domain",
    keywords = "stem porter porter2 lovins paice husk",
    url = "UPDATE-URL",
    
    zip_safe = True,
    
    classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: Public Domain",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing :: Linguistic",
    ],
    
)
