# # syntax
# class myclass:
#     # hidden member of myclass
#     __hiddenvariable = 10
# # driver code
# obj = myclass()
# obj.myclass__hiddenvariable()



class myclass():
    # hidden member of myclass
    __salary = 15000
    def add(self,increment):
        self.__salary +=increment
        print(self.__salary)

# object
obj = myclass()
obj.add(5000)
# this line causes error 
# print(obj.__salary)




