#Accept N strings, and check how many of them possess the string X
n = int(input("Enter the number of strings: "))
strings = []
count=0

print("Enter the strings:")
for i in range(n):
    string = input()
    strings.append(string)
for string in strings:
    if(string.count('X')):
        count+=1
print(f'no:of strings possess X in it={count}')
