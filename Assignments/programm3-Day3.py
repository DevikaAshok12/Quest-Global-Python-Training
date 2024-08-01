#print smallest and higgest sized string from a list of N strings
n = int(input("Enter the number of strings: "))
strings = []

print("Enter the strings:")
for i in range(n):
    string = input()
    strings.append(string)

# Initialize smallest and largest strings with the first string
smallest_string = strings[0]
largest_string = strings[0]

# Iterate through the list to find the smallest and largest strings by length
for string in strings[1:]:
    if len(string) < len(smallest_string):
        smallest_string = string
    if len(string) > len(largest_string):
        largest_string = string


print("Smallest string by length:", smallest_string)
print("Largest string by length:", largest_string)