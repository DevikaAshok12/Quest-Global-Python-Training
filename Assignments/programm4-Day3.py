#remove negative numbers from list of N numbers
n=int(input("Enter the no:of elements"))
numbers=[]
print("Enter the numbers:")
for i in range(n):
    number=int(input())
    numbers.append(number)
for number in numbers:
    if(number < 0):
        numbers.remove(number)
print("List after removing negative elements:", numbers)

