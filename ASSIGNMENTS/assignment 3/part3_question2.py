fruits = ["apple", "raspberry", "pineapple", "cherry"]

if "apple" in fruits:
    print("apple is at", fruits.index("apple"))

    
fruits[1:3] = ["orange"]

fruits.insert(2, "apricot")

fruits.extend(['car', 'bike', 'aeroplane'])

print(fruits)
