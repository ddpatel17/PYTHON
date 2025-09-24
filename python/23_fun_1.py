            # 4 types of function

#default function
d ="diya patel"
len(d) 
print(d)

# user define function
 #with parameter with return 
def addition(number):# with perameater 
    d =number + number
    return d # with return statement
  
   # calling function
number = int(input("Enter your Number "))  
ans = addition(number)
print("addition is =",ans) 


  #without parameter without return 
def greet(): # without parameter
      print("hello,my name is diya ")# without return statement
greet() # calling function


 # wihout parameter with return

import datetime

def get_current_datetime():
    return datetime.datetime.now()

# Calling the function
current_time = get_current_datetime()
print("Current Date and Time:", current_time)


 # wih parameter without return

month =int(input("Enter the month number"))

def monthcount(month):
    if month == 1:
        print("january")
    elif month == 2:
        print("february")
    elif month == 3:
        print("march")
    elif month == 4:
        print("april")
    elif month == 5:
        print("may")
    elif month == 6:
        print("june")
    elif month == 7:
        print("july")
    elif month == 8:
        print("august")
    elif month == 9:
        print("september")
    elif month == 10:
        print("october")
    elif month == 11:
        print("november")
    elif month == 12:
        print("december")
    else:
        print("Invalid month number")
monthcount(month)



