            # example:1
def add():
    return 0
def add(a):
    return a+a
def add(a,b):
    return a+b

# print(add(1)) # TypeError: add() missing 1 required positional argument: 'b'
# print(add(7)) # ypeError: add() missing 1 required positional argument: 'b'
print(add(1,5)) # 6




            # example:2
def add(a=0,b=0):
    if a==0 and b==0:
        return 0
    elif (a!=0 and b==0):
        return a+a
    elif (a==0 and b!=0):
        return b+b
    elif (a!=0 and b!=0):
        return a+b

print(add())
print(add(1))
print(add(0,7))
print(add(1,5))



            # example:3
class pet:
    def dog(self,name=None):
        if name is not None:
            print('doggy' + name)
        else:
            print('my pet cat name is minii...')
# object
obj = pet()
obj.dog()
obj.dog(' ')
obj.dog('\n filgu')




