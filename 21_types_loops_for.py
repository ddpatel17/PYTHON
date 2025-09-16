name = input("enter your name ")
vowels = ('a','e','i','o','u')
name = str.lower(name)
print(name)
count = 0
i = 0
n = len(name)
for i in range(0,n):
    print(i)
    if name[i] in vowels:
        count = count + 1
        print(count)
print ("number of vowels in name is", count)



n = input("enter the number ")
days = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")

for day in days:
    print("today is", day)