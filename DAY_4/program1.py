#create the series 1 2 2 3 3 5 5 7 8 11 13
#odd position---->1 2 3 5 8 13
#even position---->2 3 5 7 11
import math 
def check_if_prime(num):
    if(num<2):
        return False
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def nth_prime(num):
    j = 0
    if num == 1:
        j = 2
    elif num == 2:
        j = 3
    else:
        count = 2
        j = 4 #Number in J is checked if Prime or not
        while count<=num:
            if check_if_prime(j):
                count += 1
            if count==num:
              break
            j += 1
    
    return j

def nth_fibo(n):
    first= 1
    second = 2
    third=0
    if n==1:
        return first
    elif n==2:
        return second
    else:
        count=2
        while(count<n):
            third=first+second
            first = second
            second = third
            count+=1
        return third

n=int(input("Enter the number of terms:"))
i=1
while(i<=n):
    if( i%2 != 0):
        number=nth_fibo((i // 2) + 1)
    else:
        number=nth_prime(i//2)
    print(number)
    i+=1





