class account():
    def __init__(self,name,acctype,balance):
        self.name = name
        self.acctype = acctype
        self.__balance = balance

# object
obj = account("diya","saving",7000)
obj.name()
obj.acctype()
obj.balance()
obj.__balance()