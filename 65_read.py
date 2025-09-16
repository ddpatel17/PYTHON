# write a program that find no of character in file
# find vowels and consonents of file

name = input("enter file name = ")
file= open(name,"r")

vowel = ["a","e","i","u","o"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = [" ","/","!"]

vv=0
cc=0
nc=0
sy=0

count = 0

for i in file.read():
    count +=1
    if i in vowel:
        vv+=1
    elif i in numbers:
        nc+=1
    elif i in symbols:
        sy+=0

    else:
        cc+=1  



print("count= ",count)
print("vowel =",vv)
print("numbers = ",nc)
print("consonantes =",cc)
print("symbols =",sy)
