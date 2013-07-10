# Time Struct is:
# tm_year=1900, tm_mon=4, tm_mday=16, tm_hour=19, tm_min=35, tm_sec=41, tm_wday=0, tm_yday=106, tm_isdst=-1
__bucket_types = {
        'year'   : lambda t: tuple(map(lambda x: int(x), (t.tm_year))), 
        'month'  : lambda t: tuple(map(lambda x: int(x), (t.tm_year, t.tm_mon))), 
        'day'    : lambda t: tuple(map(lambda x: int(x), (t.tm_year, t.tm_mon,  t.tm_mday))), 
        'hour'   : lambda t: tuple(map(lambda x: int(x), (t.tm_year, t.tm_mon,  t.tm_mday,  t.tm_hour))), 
        'minute' : lambda t: tuple(map(lambda x: int(x), (t.tm_year, t.tm_mon,  t.tm_mday,  t.tm_hour,  t.tm_min))), 
        'second' : lambda t: tuple(map(lambda x: int(x), (t.tm_year, t.tm_mon,  t.tm_mday,  t.tm_hour,  t.tm_min,  t.tm_sec))), 
        }

"""Returns a list of time bucket types."""
def get_bucket_names():
    return __bucket_types.keys()

"""for a given timestamp, return the bucket tuple."""
def get_bucketizer(bucket_by):
    try:
        return __bucket_types[bucket_by]
    except KeyError:
        raise ValueError("%s is not a valid bucket type" % bucket_by)

