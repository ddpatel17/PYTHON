    # ceil(x)-return the smallest integer greater than or equal to x.
import math
number =float(input("enter the number ")) 
# ceil = math.ceil(number)
# print(ceil) #positive = input-2.25=3,
# negative = input-(-2.25)=-2


    #floor(x)-return the largest integer lessthan or equal to x.
floor = math.floor(number)
print(floor)#positive = input-(2.25)=2,
# negative = input-(-2.25)=-3


    #factorial- 


import math
x =float(input("enter the number "))
prinr("ceil is =", math.ceil(x)) #ceil(x)return the smallest integer greater than or equal to x.
prinr("floor is =", math.floor(x)) #floor(x)return the largest integer lessthan or equal to x.
prinr("copysign is =", math.copysign(x,2)) #copysign(x,y)return x with the sign of y
prinr("fabs is =", math.fabs(x)) # fabs(x)return theabsolute value of x
prinr("factorial is =", math.factorial(x)) #factorial(x)return the factorial of x
prinr("fmod is =", math.fmod(x,2)) # fmod(x,y)return the reminder when x is divided by y
prinr("isfinite is =", math.isfinite(x)) # isfinite(x) return true if x is neither an infinity nor a nan (not a number)
prinr("isinf is =", math.isinf(x)) # isinf(x)return true is x is a positive or negative infinity
prinr("isnan is =", math.isnan(x)) # isnan(x)return true if x is a nan
prinr("indexp is =", math.imdexp(x,i)) # return x*(2**i)