import math as m
x =float(input("enter the number "))

prinr("ceil is =", m.ceil(x)) #ceil(x)return the smallest integer greater than or equal to x.
prinr("floor is =", m.floor(x)) #floor(x)return the largest integer lessthan or equal to x.
prinr("copysign is =", m.copysign(x,2)) #copysign(x,y)return x with the sign of y
prinr("fabs is =", m.fabs(x)) # fabs(x)return theabsolute value of x
prinr("factorial is =", m.factorial(x)) #factorial(x)return the factorial of x
prinr("fmod is =", m.fmod(x,2)) # fmod(x,y)return the reminder when x is divided by y
prinr("isfinite is =", m.isfinite(x)) # isfinite(x) return true if x is neither an infinity nor a nan (not a number)
prinr("isinf is =", m.isinf(x)) # isinf(x)return true is x is a positive or negative infinity
prinr("isnan is =", m.isnan(x)) # isnan(x)return true if x is a nan
prinr("indexp is =", m.imdexp(x,i)) # return x*(2**i)