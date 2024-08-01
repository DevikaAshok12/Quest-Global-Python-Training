#Count the number of Prime digits in a number
number=input("Enter the number")
count=0
def is_prime(num):
    flag = True
    if int(num)>1:
        for i in range(2,num): 
            if (num%i)==0:
                flag = False
                break
    else:
        flag=False
    return flag

for i in number:
    if(is_prime(int(i))):
        count+=1
print(count)