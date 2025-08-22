 #Prime number

def prime(num):
    if num > 1:
        return False    
    for i in range(2,num):      
        if num % i == 0:    
            return False

num = int(input("Enter a value: "))
result = prime(num)
print(result)
    
            
