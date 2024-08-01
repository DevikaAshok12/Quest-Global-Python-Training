#Print X shape made up of stars of n lines
import sys
number_lines=int(input("Enter the number of lines u want to print:"))
if (number_lines % 2)==0:
    print("Error:Enter a odd number")
    sys.exit(0)
for i in range(1,number_lines+1):
    for j in range(1,number_lines+1):
        if( i==j or j==number_lines-i+1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()