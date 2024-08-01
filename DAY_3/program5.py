#Find sum of the series:1 + n - n(2) + n(3) - ..... m terms
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
sum=0
for i in range(0,m):
    term=(n**i)*((-1)**i)
    print(term)
    sum+=term
print(f"sum of series is {sum}")
