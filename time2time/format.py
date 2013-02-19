# linux, OSX System Log: Feb 19 00:31:32
system_fmt = "^%b %d %H:%M:%S"

# perseids log 68.201.44.180 [19/Feb/2013:17:42:44 +0000]
perseids_fmt = "[%d/%b/%Y:%H:%M:%S %z]"

__human_names = {
        "systemlog":system_fmt,
        "perseids":perseids_fmt,
        }

"""Takes in a human name for a format and returns a strftime format string."""
def get_format_string(input_format):
    if __human_names.has_key(input_format):
        return __human_names[input_format]
    else:
        return input_format

