        #strftime() function
# how to convert one format date into another format
from datetime import datetime as dt
current = dt.datetime.now()
print(current)#now has datetime in Y%M%d H%M%S
t = now.strftime("%H:%M:%S")
print("time =",t)

s1 = now.strftime("%m:%d:%Y, %H:%M:%S")# mm/dd/YY H:M:S format
print("s1 =",s1)
s2 = now.strftime("%d:%m:%Y, %H:%M:%S")# dd/mm/YY H:M:S format
print("s1 =",s2)


        #Strptime() function
birth_date = input("give your birthdate in dd-mm-yyyy format")
print(birth_date)
us_format_date = datetime.strptime(birth_date,'%d-%m-%Y')
print(us_format_date.strftime('%A %m-%d-%Y'))