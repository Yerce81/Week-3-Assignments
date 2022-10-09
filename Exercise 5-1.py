Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time
time.time()
1665346229.5929592
seconds = time.time()
print("Seconds since epoch=", seconds)
Seconds since epoch= 1665346255.5734174
day = 86400 # seconds in a day
print(seconds/day)
19274.840920988627
days = 19274.840920988627
local_time = time.cttime(days)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    local_time = time.cttime(days)
AttributeError: module 'time' has no attribute 'cttime'. Did you mean: 'ctime'?
local_time = time.ctime(days)
print(local_time)
Wed Dec 31 21:21:14 1969
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
13:30:16
print("%c", t)
%c time.struct_time(tm_year=2022, tm_mon=10, tm_mday=9, tm_hour=13, tm_min=30, tm_sec=16, tm_wday=6, tm_yday=282, tm_isdst=1)
current_time = time.strftime("%c", t)
print(current_time)
Sun Oct  9 13:30:16 2022
print((curent_time)- (local_time))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print((curent_time)- (local_time))
NameError: name 'curent_time' is not defined. Did you mean: 'current_time'?
print(current_time - local_time)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(current_time - local_time)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(int(current_time) - int(local_time))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(int(current_time) - int(local_time))
ValueError: invalid literal for int() with base 10: 'Sun Oct  9 13:30:16 2022'
year = 365 # days in a year
time_lapsed = 2022 -1969
ptint
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ptint
NameError: name 'ptint' is not defined. Did you mean: 'print'?
time_lapsed = 2022 -1970
print(time_lapsed)
52
print(year*time_lapsed)
18980
