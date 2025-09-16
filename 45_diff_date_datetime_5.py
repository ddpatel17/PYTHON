  #how to find gap between two date?
#gap between date using date class
from datetime import datetime, date
t1 = date(year = 2025, month = 6, day = 24)
t2 = date(year = 2004, month = 5, day = 14)
t3 = t1 - t2
print("t3 =",t3)

#gap between date using datetime class
t4 = date(year = 2025, month = 6, day = 24, hour = 20, minute = 50, second = 8)
t5 = date(year = 2004, month = 5, day = 14, hour = 10, minute = 60, second = 4)
t6 = t5 - t6
print("t5 =",t5)
print("total seconds =", abs(t6.total_seconds())) #different in second
