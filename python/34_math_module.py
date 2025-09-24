import math as m
x =float(input("enter the number "))

print("modf is =", m.modf(x)) # modf(x)Returns the fractional and integer parts of x
print("trunc is =", m.trunc(x))# trunc(x)Returns the truncated integer value of x
print("exp is =", m.exp(x))# exp(x)Returns e**x
print("expm1 is =", m.expm1(x))# expm1(x)Returns e**x - 1
# print("log is =", m.log(x[ ,base]))# log(x[, base])Returns the logarithm of x to the base (defaults to e)
# print("log1p is =", m.log1p(x))# log1p(x)returns the natural logarithm of 1+x
# print("log2 is =", m.log2(x))# log2(x)Returns the base-2 logarithm of x
# print("log10 is =", m.log10(x))# log10(x)Returns the base-10 logarithm of x
print("pow is =", m.pow(x,2))# pow(x, y)Returns x raised to the power y
# print("sqrt is =", m.sqrt(x))# sqrt(x)Returns the square root of x
