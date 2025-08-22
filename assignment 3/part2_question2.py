student = ["Tahir", 44, "AI and Data Science", True]

print("Student Data:")
for i in student:
    print(i)



strings = []
numbers = []
booleans = []

for i in student:
    if type(i) == str:
        strings.append(i)

    elif type(i) == int or type(i) == float:
        numbers.append(i)

    elif type(i) == bool:
        booleans.append(i)

print("Strings: ", strings)
print("Numbers: ", numbers)
print("Booleans: ", booleans)
