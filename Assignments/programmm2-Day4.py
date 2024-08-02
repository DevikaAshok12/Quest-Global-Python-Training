#Accept N strings and count the number of Palindromes in it.
def palindrome(string):
    count = 0
    for string in strings:
        if (string==string[::-1]):
            count += 1
    return count

n = int(input("Enter the number of strings: "))
strings = []
count=0

print("Enter the strings:")
for i in range(n):
    string = input()
    strings.append(string)
print(strings)
palindrome_count=palindrome(strings)
print(palindrome_count)
