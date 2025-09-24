book={}
print(book)

book['brand_name']='puma'
book['item']='shoes' 
book['price']=12000
print(book)

# copy
d1=book.copy()
print(d1)
d1

# del d1['price']# delete value in only d1 dic
print(d1)
print(book)

# items
print(book.items())

# keys
print(book.keys())

# values 
print(book.values())

# pop
print(book.pop('price',12000))
print (book)

# popitem
print(book.popitem())
print(book)

# clear 
print(book)
book.clear()

