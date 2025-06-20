
Alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digit=['0','1','2','3','4','5','6','7','8','9']
Special=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

s = ","
print(s.join(Alphabets + digit + Special))


import random as r
import string as s


def generate_password(length):

        if length < 4:
            print("password length must be at least 4.")

        elif length > 20:
              print("password length must be at most 20.")
    
        else:
            password = [
                r.choice(s.ascii_lowercase),
                r.choice(s.ascii_uppercase),
                r.choice(s.digits),
                r.choice(s.punctuation)
            ]
            
            r.shuffle(password)
            
            for i in range(length - 4):
                password += [r.choice(s.ascii_uppercase + s.ascii_lowercase + s.digits + s.punctuation)]
            r.shuffle(password)
            # return ''.join(password)
            n = int(input("enter a length of password: "))
            ans = (generate_password)
            print(ans)
            print(generate_password(n))
            # if ans:
            #     print("Generated password:", ans)
            # len = int(input("enter a length of password: "))
            # password = p.generate_password(len)

            print("\n password is",generate_password)
            print("\n lenght of password is",len(password))
            save_password(generate_password)






def save_password(password):
    file_name = "generate_password.txt"
    with open(file_name,'a') as file:
        file.write(password + '\n' )
   