#!/usr/bin/env python

from distutils.core import setup

setup(
    name='TGrep',
    version='0.1.0',
    author='Andrew Thomson',
    author_email='athomsonguy@gmail.com',
    packages=['tgrep', 'tgrep.test'],
    scripts=['bin/tgrep'],
    url='http://pypi.python.org/pypi/TGrep/',
    license='LICENSE.txt',
    description='Tools for comparing timestamps.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
