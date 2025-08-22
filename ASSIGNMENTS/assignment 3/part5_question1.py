def age_group(age):
    if age < 18:
        print("Minor")

    elif age < 60:
        print("Adult")

    else:
        print("Senior citizen")

age = int(input("Enter your age: "))

age_group(age)
