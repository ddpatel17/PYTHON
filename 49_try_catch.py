try:
    age = int(input("enter your age at the first day of job "))
    if age<18 or age>60:
        raise ValueError
    else:
        remain_age = 60-age
        print(f"you have remain {remain_age} year for do job")    
except ValueError:
    print("not capable for job ")

print("good bye")