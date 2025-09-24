box1 = 20
box2 = 20
box3 = 30
box4 = 50

# is
result = box1 is box2
print("result =",result) # true
result = box3 is box4
print("result =",result) #false 
print("result =",result,id(box1),id(box2),id(box3),id(box4))

# is not
result = box1 is not box2
print("result =",result) #false 
result = box3 is not box4
print("result =",result) # true
print("result =",result,id(box1),id(box2),id(box3),id(box4))