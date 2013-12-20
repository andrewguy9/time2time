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
    date = match.group()
    return date

def get_time(format_str, line):
    """Takes a line and finds a time which matches the expr"""
    date = get_time_str(format_str, line)
    if date is None:
        return None
    else:
        return strptime(date, format_str)
