
Alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit=['0','1','2','3','4','5','6','7','8','9']
Special=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

s = ","
print(s.join(Alphabets + digit + Special))


import random as r


def getpassword(length =8):
    lower = string.lowercase
    upper = string.uppercase
    digit = string.digit
    special = string.special

    # for i in range()
        
        if length == 12:
            return str(r.shuffle(lower)) + str(r.shuffle(lower)) + str(r.shuffle(lower)) + str(r.shuffle(upper)) + str(r.shuffle(upper)) + str(r.shuffle(upper)) + str(r.shuffle(special)) + str(r.shuffle(special)) + str(r.shuffle(digit)) + str(r.shuffle(digit)) + str(r.shuffle(digit)) + str(r.shuffle(digit))

        elif length == 8:
            return str(r.shuffle(lower)) + str(r.shuffle(lower)) + str(r.shuffle(upper)) + str(r.shuffle(upper)) + str(r.shuffle(special)) + str(r.shuffle(digit)) + str(r.shuffle(digit)) + str(r.shuffle(digit))
        elif length == 4:
            return str(r.shuffle(special)) + str(r.shuffle(lower)) + str(r.shuffle(upper)) + str(r.shuffle(digit)) 
        else:
            return "invalid length"

n = int(input("enter the number of password "))  
# d =(getpassword)
print(getpassword(n))     