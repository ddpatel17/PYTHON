try:
    n1 = int(input("enter the value of n1 "))
    n2 = int(input("enter the value of n2 "))
    division = n1/n2
    print(f"division is = {division}")
except ValueError:
    print("invalid input enter only numeric value")
except ZeroDivisionError:
    print("Zero is not valid")