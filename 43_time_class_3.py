     # time class
#How to create time object from given hour, minute, second
from datetime import time
anytime = time(11,20,50,2)
anytime = time(11,20,50)
print("hour =",anytime.hour)
print("minute =",anytime.minute)
print("second =",anytime.second)
print("microsecond =",anytime.microsecond)
