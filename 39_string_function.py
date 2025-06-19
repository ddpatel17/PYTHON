name = "The Easylearn Academy"
print(name.upper())
print(name.lower())
print("length =", len(name))
print(name)

       # Method that return Boolean value
print("isalnum =",str.isalnum(name))  # str.isalnum() String consists of only alphanumeric characters (no symbols)
print("isalpha =",str.isalpha(name))  # str.isalpha() String consists of only alphabetic characters (no symbols)
print("islower =",str.islower(name))  # str.islower() String's alphabetic characters are all lower case
print("isupper =",str.isupper(name))  # str.isupper() String's alphabetic characters are all upper case
print("isnumeric =",str.isnumeric(name)) # str.isnumeric() String consists of only numeric characters 
print("isspace =",str.isspace(name)) # str.isspace() String consists of only whitespace characters # "\t", " " , "\t \n"
print("istitle =",str.istitle(name)) # str.istitle() String is in title case

# join()
list = ["India","usa","UK","Canada","Australia"]
s = ","
print (s.join(list))
print(",".join(list))

# replace()
name = "the easylearn Academy"
print("replace =",name.replace('the','The'))
print("replace =",name.replace('e','E',1))
print("replace =",name.replace('e','E',2))
print("replace =",name.replace('easylearn','Easylearn',2))