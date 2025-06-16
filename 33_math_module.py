import math as m
x =float(input("enter the number "))

print("ceil is =", m.ceil(x)) #ceil(x)return the smallest integer greater than or equal to x.
print("floor is =", m.floor(x)) #floor(x)return the largest integer lessthan or equal to x.
print("copysign is =", m.copysign(x,2)) #copysign(x,y)return x with the sign of y
print("fabs is =", m.fabs(x)) # fabs(x)return theabsolute value of x
# print("factorial is =", m.factorial(x)) #factorial(x)return the factorial of x
print("fmod is =", m.fmod(x,2)) # fmod(x,y)return the reminder when x is divided by y
print("isfinite is =", m.isfinite(x)) # isfinite(x) return true if x is neither an infinity nor a nan (not a number)
print("isinf is =", m.isinf(x)) # isinf(x)return true is x is a positive or negative infinity
print("isnan is =", m.isnan(x)) # isnan(x)return true if x is a nan

# print("indexp is =", m.imdexp(x,)) # return x*(2**i)