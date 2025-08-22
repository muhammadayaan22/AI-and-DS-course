def larger_number(num1, num2):
    if num1 > num2:
        print(f"{num1} is largest.")

    else:
        print(f"{num2} is largest")
        
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

larger_number(num1, num2)
