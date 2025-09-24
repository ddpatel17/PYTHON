import random as r
def getotp(size =6):
     if size == 8:
         return str(r.randint(10,90)) + str(r.randint(10,90)) + str(r.randint(10,90)) + str(r.randint(10,90))
     elif size == 6:
         return str(r.randint(10,90)) + str(r.randint(10,90)) + str(r.randint(10,90))
     elif size == 4:
         return str(r.randint(10,90)) + str(r.randint(10,90))     
     elif size == 2:
         return str(r.randint(10,90))
     else:
         return 0
        
n = int(input("enter the size of otp "))  
ans =(getotp)
print(ans)  
print(getotp(n))
   





