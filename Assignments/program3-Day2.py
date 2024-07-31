#second smallest digit in a number
number=input("Enter the number:")
smallest=int(number[0])
largest=int(number[0])
for i in number:
    if(int(i)<smallest):
        smallest=int(i)
    if(int(i)>largest):
        largest=int(i)

sec_smallest=largest
for i in number:
    if int(i)>smallest and int(i)<sec_smallest:
        sec_smallest=int(i)
print(f'Second smallest digit is {sec_smallest}')

