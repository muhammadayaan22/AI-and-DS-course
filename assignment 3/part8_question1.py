def area_circumference(radius):
    area = 3.14 * radius
    circumference = 3.14 * radius **2
    return area, circumference
    
radius = int(input("Enter a value: "))
result = area_circumference(radius)
print(result)
