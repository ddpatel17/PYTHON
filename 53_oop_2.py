# create a class for calculate add,sub,div,mul for numbers
class calculator:
    # constructor
    def __init__(self):
        print("constructor called")

    # arbitary function 
    def add(self,*n):
        sum = 0
        for i in n:
            sum = i+sum
        return sum

    def sub(self,*n):
        sum = 0
        for i in n:
            sum = i-sum
        return sum

    def mul(self,*n):
        sum = 1
        for i in n:
            sum  = i*sum
        return sum

    def div(self,a,b):
        sum = a/b
        return sum


c1 = calculator()
print(c1.add(10,10,10,10,10))
print(c1.sub(2,3,4))
print(c1.mul(1,2,3,4,5))
print(c1.div(10,2))


        

