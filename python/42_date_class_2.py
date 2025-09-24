# datetime.date class 
import datetime as dt
birth_date = dt.date(2004,5,14)
print(birth_date)
      # or
from datetime import date
birth_date = date(2004,5,14)
print(birth_date)


# timestamp 
      # How to get current time stamp
from datetime import datetime
ts = datetime.now().timestamp()
print("timestamp: ", ts) # float
print("timestamp :", int(ts)) #int
      # How to Get date from a timestamp?
import datetime as dt
ts = dt.date.fromtimestamp(1750393592)
print("date =", ts)
     # or 
from datetime import date 
ts = date.fromtimestamp(1750393592)
print("date =", ts)  
  

  

 






