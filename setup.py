#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Time2Time',
    version='0.1.0',
    author='Andrew Thomson',
    author_email='athomsonguy@gmail.com',
    packages=['time2time', 'time2time.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/Time2Time/',
    license='LICENSE.txt',
    description='Tools for comparing timestamps.',
    long_description=open('README.txt').read(),
)
