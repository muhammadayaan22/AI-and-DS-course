a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

if a > b:
    print(f"{a} is greater.")

elif b > a:
    print(f"{b} is greater.")
elif c >= b and c >= a:
    print(f"{c} is greater.")
    
else:
    print(f"{c} is the ;argest.")
