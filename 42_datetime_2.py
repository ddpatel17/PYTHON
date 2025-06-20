# datetime.date class 
import datetime as dt
birth_date = daatetime.date(2004,5,14)
print(birth_date)
      # or
from datetime import date
birth_date = date(2004,5,14)
print(birth_date)


# timestamp 
      # How to get current time stamp
import datetime as dt
ts = dt.now().timestamp()
print("timestamp: ", ts) # float
print("timestamp :", int(ts)) #int
      # How to Get date from a timestamp?
from datetime import date
ts = date.fromtimestamp(1750393592)
print("date =", ts)
