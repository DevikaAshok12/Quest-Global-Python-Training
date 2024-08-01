#accept n numbers from user and swap the consecutive elements in the list
n = int(input("Enter the number of elements: "))
lst = []

# Prompt the user to enter the numbers
print("Enter the numbers:")
for i in range(n):
    number = int(input())  # Read each number
    lst.append(number)  # Append the number to the list
print("Original list:", lst)
for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
print("List after swapping consecutive elements:", lst)