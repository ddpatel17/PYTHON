import math 
list = [20,'d',10,300,'D']
print(list)
sum = 0
for item in list:
    print(item)
    try:
        if not isinstance(item,float): 
            sum += item
    except:
        print(f"invalid item skipped {item}")
print(f"sum is = {sum}")
        
