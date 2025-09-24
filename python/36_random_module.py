import random as r
print("float random number is",r.random(),"-",r.random(),"-",r.random())


# uniform()
print("float random number through uniform is",r.uniform(81,88))

#randint() & randrange()
print("randint integer number",r.randint(1,5))
print("randrange integer number",r.randrange(1,10,2)) 

# choice() & choices()
roll_no=["1","2","3","33","35","50"]
print(r.choice(roll_no))
print(r.choices(roll_no,k=2))

#shuffle()
number_list = [5,10,15,20,25,30,35,40,45,50]
print(number_list)
r.shuffle(number_list)
print("first shuffle:",number_list)
r.shuffle(number_list)
print("second shuffle:",number_list)


#sample()
print(r.sample(number_list,10))


