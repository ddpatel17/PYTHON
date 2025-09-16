import datetime
import math
import sys
def showmethods(module):
    list = dir(module)
    print("----------------------------------------------")
    print("method in math module",module)
    for item in list:
        print(item)
    
showmethods(datetime)
showmethods(math)
showmethods(sys)

