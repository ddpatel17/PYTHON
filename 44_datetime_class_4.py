        # datetime class
#how to create datetime object that has both date and time
#For only date use
from datetime import datetime 
datetime(year,month,day)
a = datetime(2025,6,24)
print(a)

# for both date and time use
datetime(year,month,day,hour,minute,second,microsecond)
b = datetime(2025,6,24,4,25,59,22)
print(b)
print("year =",b.year)
print("month ="b.month)
print("day =",b.day)
print("hour =",b.hour)
print("minute =",b.minute)
print("second =",b.second)
print("microsecond ="b.microsecond)
print("timnestamp =",b.timestamp())
