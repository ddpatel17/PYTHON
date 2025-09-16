# how to open file 
# obj = open("practice.txt")
# print("file is opened ")
# print(obj)

# obj.close()



obj = open("practice.txt")
print("file is opened ")
print(obj)

for i in obj:
    for j in i:
        print(j)

print(obj.read(3))
obj.close()
