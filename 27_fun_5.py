                #recursion function 

def calc_mul(x):
    if x == 1:
        return 1
    else:
        return(x*2)
num = 2
print("the mul of", num,"is", calc_mul(num))




# SECOND EXAMPLE

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = 4
print("The factorial of", num, "is", calc_factorial(num))
