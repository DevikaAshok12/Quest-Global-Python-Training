string1 = input("Enter the first string  ")
string2 = input("Enter the second string ")
try:
    print(int(string1) + int(string2))
except ValueError:
    print(string1 +" "+string2)