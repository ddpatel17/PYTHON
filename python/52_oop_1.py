class person:
    def walk(self):
        print("i can walk....")
        
    def talk(self):
        print("i can talk....")
        
    def detalis(self,name,age):
        print(f"name is = {name}")
        print(f"age is = {age}")
    
    def bank_detailes(self,Ac_no,ifsc):
        print(f"Ac_no is {Ac_no} in SBI saving account")
        print(f"ifsc is {ifsc} in SBI saving account")

        
        
p1 = person()
p1.walk()
p1.talk()
p1.detalis("diya",22)
p1.bank_detailes(12345678910,'SBI0123456')

p1=person()
print(p1.walk())
print(p1.talk())
print(p1.detalis("diya",22))
print(p1.bank_detailes(12345678910,'SBI0123456'))

p2 = person()
p2.detalis("DIYA",22)
p2.bank_detailes(55555555555,'SBI0123456')

p3 = person()
p3.walk()
p3.talk()