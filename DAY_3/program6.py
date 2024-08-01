#Find sum of the series:n - n(2)/3 + n(4)/5 - n(8)/7 + ..... upto m terms  and (1<=n<=5) and (2<m<10)
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
sum=0
sign=1
power=1
if(1<=n<=5 and 2<m<10):
    for i in range(1,m+1):
        term = sign * (n ** power) // (2 * i - 1)
        #print(term)
        sum += term
        sign *= -1
        power *= 2
        
print(f"sum of series is {sum}")
