"""
Calling datetime.datetime.fromtimestamp() and passing it 1000000
returns a datetime object for the moment 1,000,000 seconds after the
Unix epoch. Passing time.time(), the Unix epoch timestamp for the
current moment, returns a datetime object for the current moment. So
the expressions datetime.datetime.now() and
datetime.datetime.fromtimestamp(time.time()) do the same thing; they
both give you a datetime object for the present moment.
"""
import datetime,time
a=datetime.datetime.now()
print(a)
print(a.month)
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
#create own datetime object
print(dt)
print(datetime.datetime.fromtimestamp(time.time()))