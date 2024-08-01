# Number of terms for the Fibonacci series
n = int(input("Enter the limit:"))

# Initialize the first two terms of the Fibonacci series
first= 1
second = 2

# Print the first two terms
print(first, second, end=" ")

# Generate and print the rest of the Fibonacci series up to n terms
for i in range(2, n):
    next_term = first + second
    print(next_term, end=" ")
    first = second
    second = next_term