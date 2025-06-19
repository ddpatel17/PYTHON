
Alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit=['0','1','2','3','4','5','6','7','8','9']
Special=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

s = ","
print(s.join(Alphabets + digit + Special))


import random as r


def getpassword(size =8):


    # for i in range(size =8):
        
        if size == 12:
            return str(r.choice(ascii_lower)) + str(r.choice(ascii_lower)) + str(r.choice(ascii_lower)) + str(r.choice(ascii_upper)) + str(r.choice(ascii)) + str(r.choice(ascii_up)) + str(r.choice(spece)) + str(r.choice(spece)) + str(r.choice(digit)) + str(r.choice(digit)) + str(r.choice(digit)) + str(r.choice(digit))

        elif size == 8:
            return str(r.choice(ascii_lower)) + str(r.choice(ascii_lower)) + str(r.choice(ascii_upper)) + str(r.choice(ascii_upper)) + str(r.choice(special)) + str(r.choice(digit)) + str(r.choice(digit)) + str(r.choice(digit))
        elif size == 4:
            return str(r.choice(special)) + str(r.choice(ascii_lower)) + str(r.choice(ascii_upper)) + str(r.choice(digit)) 
        else:
            return "invalid size"

n = int(input("enter the size of password "))  
p =(getpassword)
print(p)  