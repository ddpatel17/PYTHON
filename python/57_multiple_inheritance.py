    # multiple inheritance 
    # multiple parent class and 1 chiled class use multiple parent 

# parent class
class saving_account:
    def __init__(self,interest):
        self.interest = interest 

    def get_interest(self):
        print("interest added :",self.interest) # % error ?

class current_account:
    def __init__(self,limit):
        self.limit = limit

    def set_limit(self):
        print("limit is created :",self.limit)


# chiled class
class bank(saving_account,current_account):
    def __init__(self,interest,limit):
        saving_account.__init__(self,interest)
        current_account.__init__(self,limit)

    def get_detailes(self):
        print("bank detailes here.....")

#?
b1 = bank(10,5000)
b1.get_interest()
b1.set_limit()
b1.get_detailes()




