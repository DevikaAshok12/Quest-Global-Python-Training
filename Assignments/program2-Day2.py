#Find biggest digit in a number
number=input("Enter the number:")
largest=int(number[0])
for i in number:
    if(int(i)>largest):
        largest=int(i)
print(f'largest number is {largest}')



