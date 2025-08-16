# Prime number

num = int(input("Enter a number: "))
check = True    
if num > 1:  
    for i in range(2,num):      
        if num % i == 0:        
            print("Number is not prime")   
            check = False               
            break



if check:
    print(f"{num} is a prime number")
