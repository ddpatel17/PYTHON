d ="diya patel"
len(d) # default function
print(d)
# # user define function

def addition(number):# with perameater 
    d =number + number
    # return d # with perameater 
    print("addition =", d) # output is addition = 2
number = int(input("Enter your Number "))  
print("addition =", number) # right 
dd = addition(number)
# print("addition =",dd) # return not passed then output is addition = None



# def nsquare(x,y = 3,2)# error wy?
# def nsquare(x,y= 3): #here x is required and y is optional
# def nsquare(y=2,x=4):   # for print("result is =",nsquare())
#     return (x*x + 2*x*y + y*y) # (1*1+2*1*3+3*3)=1+6+9
# result = nsquare(1) # x=1,y=3
# print("result is =",result)
# print("result is =",nsquare(2,4)) #  x=2,y=4(2*2+2*2*4+4*4)=4+16+16
# print("result is =",nsquare(y=2,x=3)) #x=2,y=4(3*3+2*3*2+2*2)=9+12+4
# print("result is =",nsquare())  #nsquare() missing 1 required positional argument: 'x'

