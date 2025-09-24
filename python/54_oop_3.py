class student:
    def __init__(self,name,age,roll_no):
        # instance variable
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = {}
    
    def grtmarks(self):
        eng = int(input("enetr the emg marks "))
        hindi = int(input("enter the hindi marks "))
        guj = int(input("enter the guj marks "))
        self.marks['eng'] = eng
        self.marks['hindi'] = hindi
        self.guj['guj'] = guj

    def detailes(self):
        print('name ='self.name)
        print('age ='self.age)
        print('roll_no = 'self.roll_no)
        print('marks ='self.marks)

s1 = student('diya',22,51)
s1.getmarks()
s1.detailes()