    # single inharitance 
# parent class 
class person:
    # constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print("i can walk...")

    def talk(self):
        print("i can talk...")

    def detailes(self,name,age):
        print("name =",self.name)
        print("age  =",self.age)


# child class
class student(person):
    def __init__(self,name,age,roll_no,school):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.school = school

    def read(self):
        print("i can read hindi, english and gujrati language...")

    def write(self):
        print("i can write hindi, english and gujrati language...")

    def student_detailes(self):
        super().detailes()
        print("roll_no =",self.roll_no)
        print("school name =",self.school)


# object 
p1 = person('diya',22)
p1.walk()
p1.talk()
# # p1.detailes()  # error 

s1 = student('diya',22,51,'sardar patel')
s1.read()
s1.write()
# # s1.student_detailes() # error 

s1.walk()
s1.talk()
# s1.detailes()  # error 





