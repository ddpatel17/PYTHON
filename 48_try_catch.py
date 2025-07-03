import math 
list = [10,'a',20,True,30]
print(list)
sum = 0
for item in list:
    print(item)
    try:
        if non isinstance(item,bool):
            sum += item
    except:
        print(f'invalid item skipped {item}')
print(f'sum of item = {sum}')





