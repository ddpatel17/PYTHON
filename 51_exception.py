try:
    a = int(input("enter the a "))
    b = int(input("enter the b "))
except Exception as e:
    print(e)
else:
    print(a+b)
finally:
    print("good bye")



try:
    age = int(input("enter your age "))
    if age>18:
        print("you are eligible for voting")
    else:
        print("you are not eligible for voting")
except ValueError:
    print("invalid age")
except:
    print("below 18 years!!!")

