#find a number is prime or not
number=int(input("Enter the number:"))
flag = True
if number>1:
    for i in range(2,number): 
        if (number%i)==0:
            
            flag = False
            break
else:
    flag=False

if(flag):
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
                
            
        
