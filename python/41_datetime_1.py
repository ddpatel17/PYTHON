import datetime as dt
# get current date & time 
current_datetime = dt.datetime.now() # 'now' is method in datetime module
print(current_datetime)
        # date class
# get current date 
current_date = dt.date.today()
print(current_date)  

# get today yera,month,day with date object 
print("current year: ",current_date.year)
print("current month: ",current_date.month)
print("current day: ",current_date.day)