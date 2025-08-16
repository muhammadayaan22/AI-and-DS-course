num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter a operator [x,+,-,/]: ")


if operator == '+':
    print("result:", num1 + num2)

elif operator == '-':
    print("result:", num1 - num2)

elif operator == 'x':
    print("result:", num1 * num2)

elif operator == '/':
    print("result:", num1 / num2)

else:
    print("Invalid Operator")
     
