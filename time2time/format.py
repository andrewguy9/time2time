# linux, OSX System Log: Feb 19 00:31:32
system_fmt = "%b %d %H:%M:%S"

# perseids log 68.201.44.180 [19/Feb/2013:17:42:44 +0000]
perseids_fmt = "[%d/%b/%Y:%H:%M:%S +0000]"

# HTTP Format Thu, 23 May 2013 21:21:18 GMT
http_fmt = "%a, %d %b %G %H:%M:%S GMT"

__human_names = {
        "systemlog":system_fmt,
        "perseids":perseids_fmt,
        "http":http_fmt,
        }

"""Takes in a human name for a format and returns a strftime format string."""
def get_format_string(input_format):
    if __human_names.has_key(input_format):
        return __human_names[input_format]
    else:
        return input_format

"""Returns a list of (name,format_string) touples."""
def get_format_strings():
    return __human_names.items()
