    # multilevel inheritance 



                            # EXAMPLE 1
# write a program that convert bytes to kb,mb,gb
# PARENT CLASS
class bytes:
    def __init__(self,byte):
        self.byte = byte
        
    def getbytes(self):
        return self.byte

# CHILED CLASS
class kb(bytes):
    def __init__(self, byte):
        super().__init__(byte)
        
    def getkb(self):
        ans = self.byte / 1000
        return ans
        
class mb(kb):
    def __init__(self, byte):
        super().__init__(byte)
        
    def getmb(self):
        ans = super().getkb() / 1000
        return ans
    
class gb(mb):
    def __init__(self, byte):
        super().__init__(byte) 
        
    def getgb(self):
        ans = super().getmb() / 1000
        return ans
    
o1 = gb(5000)
print("bytes : ",o1.getbytes())
print("kb : ",o1.getkb())
print("mb : ",o1.getmb())
print("gb : ",o1.getgb())





                            #EXAMPLE 2
# convert seconds to minitues , hours ,day
# PARANT CLASS
class second:
    def __init__(self,sec):
        self.sec = sec
        
    def getsecond(self):
        return self.sec
    
# CHILED CLASS
class minute(second):
    def __init__(self, sec):
        super().__init__(sec)
        
    def getmin(self):
        return self.sec / 60
    
class hours(minute):
    def __init__(self, sec):
        super().__init__(sec)
        
    def gethours(self):
        return super().getmin() / 60
    
class days(hours):
    def __init__(self, sec):
        super().__init__(sec)
        
    def getdays(self):
        return super().gethours() / 24
    
obj = days(3600)
print(obj.getsecond())    
print(obj.getmin())    
print(obj.gethours())    
# print(obj.getdays()) 
day = obj.getdays()   
print(round(day,2))