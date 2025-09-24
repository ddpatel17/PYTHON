# keywords arguments function
def items(cashew,almond,dates):# with perameater without return
    print('items in : cashew -',cashew,'almond -',almond,'dates -',dates)
items(3000,3000,1500)
items(cashew=3000,dates=1500,almond=3500,)

# default arguments function

# if we write x=y=10 than both get same value
def nsquare(x, y = 2): #here x is required and y is optional
    return (x*x + 2*x*y + y*y)
result = nsquare(3)  # 3*3 +2*3*2 +2*2
print("result is = ",result)
print("result is =",nsquare(2,3))
print("result is =",nsquare(1))  #nsquare() missing 1 required positional argument: 'x'
print("result is =",nsquare(y=2,x=3))

