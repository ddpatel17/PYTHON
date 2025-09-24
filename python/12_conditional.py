a =int(input("enter the value of a "))
b =int(input("enter the value of b "))
c =int(input("enter the value of c "))
d =int(input("enter the value of d "))

# and 
print("and operator",(a==b and c==d))
print("and operator",(a==b & c==d)) # alwsays false 

# or 
print("or operator",(a==b or c==d))
print("or operator",(a==b | c==d)) # alwsays false 

# not
print("not operation",not(a==b and c==d))


