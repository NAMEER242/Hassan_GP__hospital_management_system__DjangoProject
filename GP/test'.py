import datetime
import time


def datetime_to_ms_epoch(dt):
    microseconds = time.mktime(dt.timetuple()) * 1000000 + dt.microsecond
    return int(round(microseconds / float(1000)))


time_in_millis = 1596542285000
dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0)
print(datetime_to_ms_epoch(dt))
