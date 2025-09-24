l1=['diya','123','12.4','patel']
l2=[456,'easylearn']
print(l1);print(l2)

# append
l1.append('2025')
print(l1)

# extend
l1.extend(l2)
print(l1)

l1=['diya','123','12.4','patel'] 
# insert
l1.insert(4,'True')
print(l1)

# remove(item)
l1.remove('True')
print(l1)

# pop (position)
print(l1.pop(2))
print(l1)

# clear()
l2.clear()
print(l2)

# index()
# print(l1.index('12.4')) # error why?
# print(l1)

print(l1.index('diya')) 
print(l1)

#count(item)
print(l1.count('123')) # count how much value in list....
print(l1)

l3=[1,54,20,25,30,35,25]
l4=['abc','efg','hij']
print(l3);print(l4)

#sort() # how its work to ask?
print(l1.sort()) 
print(l1)
print(l3.sort()) 
print(l3)
l3.sort()
print(l3)

print(sorted(l3))
print(sorted(l4))

#reverse() # how its work to ask?
l3.reverse()
print(l3)

# copy()
l5=l1.copy
print(l5)

# del l5[1] # get error to ask?
del l5
print(l5)



