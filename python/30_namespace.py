amount = 2000  # amount is global variable as it is declared outside function
def addmoney(): # uncomment the following line to fix the code:
    global amount
    amount = amount + 1 # it willaccess and change global amount variable 
print (amount) # global variable not change in value 
addmoney ()
print (amount) # local variable to change 