#!/usr/bin/env python

from _strptime import TimeRE as formatGenerator
from time import strptime

fg = formatGenerator()

def get_time_match(format_str, line):
    """Takes a line and finds a regex match against the format string"""
    expr = fg.compile(format_str)
    match = expr.match(line)
    return match

def get_time_str(format_str, line):
    """Takes a line and finds a timestamp which matches the time expr"""
    match = get_time_match(format_str, line)
    if match:
        date = match.group()
        return date
    else:
        raise ValueError("%s does not occur in '%s'" % (format_str, line))

def get_time(format_str, line):
    """Takes a line and finds a time which matches the expr"""
    date = get_time_str(format_str, line)
    return strptime(date, format_str)
