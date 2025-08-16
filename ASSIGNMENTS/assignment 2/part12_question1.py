temp = int(input("Enter a your temperature: "))

if temp < 0:
    print("Freezing temperature")

elif 0 <= temp < 26:
    print("Temperature is moderate")

else:
    print("Hot Temperature")
