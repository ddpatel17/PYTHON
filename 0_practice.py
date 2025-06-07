# name=input("enter your name")
# print("your name is =",diya)
# age=input("enter your age")
# print("your age is =",20)

# # name=input("enter your name")
# # print("your name is =",name )

# # age=input("enter your age")
# # print("your age is =",age )


# num1=input("enter first number")
# num2=int(input("enter second number"))# always write in integer because applyu "int"
# num1=int(num1) # input pass in integer because "int"
# print(num1+num2)


# name1="diya"
# name="diya patel"
# print(name)
# print(name[::])
# print(name[1])
# print(name[0:5])
# # print(name[0:5:2]) #output = dy?
# print(name[:5])
# print(name[4:])
# print(name)
# print(name*2)
# print(name+""+name1)


# l1=['diya','123','12.4','patel','True']
# l2=[456,'easylearn']
# print(l1);print(l2)
# # l1[4]=False
# # print(l1+True)
# # print(l1+10)
# l1.append(20)
# print(l1)


name1="diya"
name="diya patel"

print(name1[1:2:3]) #dy?

l1=['diya','123','12.4','patel']
l2=[456,'easylearn']
l1.append('2025')
print(l1)




s ="diya patel"
len(s) # default function

# user define function

def addition(number):# with perameater 
    s =number+number
    return s # with perameater 
    # print("addition is =", s)
number = int(input("Enter your Number"))  
ans = addition(number)
# print("addition is =", ans)
print("addition =", ans)