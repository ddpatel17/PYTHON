
                # return multiple value from function 

def price(book1,book2):
    add = book1+book2
    sub = book1-book2
    mul = book1*book2
    return add,sub,mul
book1 =int(input("enter the first number "))
book2 =int(input("enter the second number "))
totalbill = price(book1,book2)
print(totalbill)


