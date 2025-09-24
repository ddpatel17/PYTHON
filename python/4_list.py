l1=['diya','123','12.4','patel']
l2=[456,'easylearn']
print(l1);print(l2)
print(l1,l2)
print(l1[1])
print(l1[0:3])
print(l1[3:5])
print(l1+l2)
print(l1*2)

l2[0]='Diya'
print(l2)
# l1[4]=True # apply append method for add value  
# print(l1+True)# get error because not possible add the value 
# print(l1+10) # get error because not possible add the value 
# print(l1)

l1.append(20) # this is right method for add value in list 
print(l1)
