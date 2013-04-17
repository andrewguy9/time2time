#!/usr/bin/env python

def split_time_str(expr, line):
    """Takes a line of input and a time expression.
    Splits the line into a timestamp and the rest of the line."""
    match = expr.match(line)
    if match:
        date = match.group()
        rest = line[match.end():]
        return (date,rest)
    else:
        return (None,line)

