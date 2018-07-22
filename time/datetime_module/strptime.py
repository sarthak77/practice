"""
If you have a string of date information, such as
'2015/10/21 16:29:00' or 'October 21, 2015', and need to convert it to
a datetime object, use the datetime.datetime.strptime() function. The
strptime() function is the inverse of the strftime() method. A custom
format string using the same directives as strftime() must be passed
so that strptime() knows how to parse and understand the string.
(The p in the name of the strptime() function stands for parse.)
"""
import datetime
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))