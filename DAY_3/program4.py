#program to print nth fibonnacci number
n=int(input("Enter the value of n:"))
first= 1
second = 2
third=0
if n==1:
    print(first)
elif n==2:
    print(second)
else:
    count=2
    while(count<n):
        third=first+second
        first = second
        second = third
        count+=1
    print(third)

        

    
