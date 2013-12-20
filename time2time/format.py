# linux, OSX System Log: Feb 19 00:31:32
system_fmt = "%b %d %H:%M:%S"

# perseids log 68.201.44.180 [19/Feb/2013:17:42:44 +0000]
perseids_fmt = "[%d/%b/%Y:%H:%M:%S +0000]"

# HTTP Format Thu, 23 May 2013 21:21:18 GMT
http_fmt = "%a, %d %b %G %H:%M:%S GMT"

__human_names = {
    "systemlog": system_fmt,
    "perseids": perseids_fmt,
    "http": http_fmt,
}


def get_format_string(input_format):
    """Takes in a human name for a format and returns
    a strftime format string."""
    if input_format in __human_names:
        return __human_names[input_format]
    else:
        return input_format


def get_format_strings():
    """Returns a list of (name,format_string) touples."""
    return __human_names.items()
