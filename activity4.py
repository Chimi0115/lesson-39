import datetime
x=datetime.datetime.now()
print("Current time is ",x)

print("Todays date is ",x.strftime("%d"))

print("Todays date is ",x.strftime("%x"))

print("Time now is ",x.strftime("%X"))

print("Hour now is ",x.strftime("%H"))

print("Minutes now is ",x.strftime("%M"))

print("Seconds now  is ",x.strftime("%S"))

import calendar

print(calendar.calendar(2025))

yy=2010
mm=1
print(calendar.month(yy,mm))