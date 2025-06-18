import random as r
def generate_otp(size =6):
    if size == 8:
        return str(r.radiant(10,90)) + str(r.radiant(10,90)) + str(r.radiant(10,90)) + str(r.radiant(10,90))
    else size == 6:
         return str(r.radiant(10,90)) + str(r.radiant(10,90)) + str(r.radiant(10,90))
    else size == 4:
         return str(r.radiant(10,90)) + str(r.radiant(10,90))     
    else size == 2:
         return str(r.radiant(10,90))
    elif:
          return 0
        
n = int(input("enter the size of otp "))  
d =(generate_otp)
print(d)      