#find smallest and biggest element in a list of numbers
n = int(input("Enter the number of elements: "))
numbers = []

print("Enter the numbers:")
for i in range(n):
    number = int(input())
    numbers.append(number)

# Initialize smallest and largest with the first element of the list
smallest = numbers[0]
largest = numbers[0]

# Iterate through the list to find the smallest and largest elements
for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
print("Smallest element:", smallest)
print("Largest element:", largest)