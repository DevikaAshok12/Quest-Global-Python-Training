#Print a hollow square of n line with the diagonals.
number_lines=int(input("Enter the number of lines u want to print"))
for i in range(1,number_lines+1):
    for j in range(1,number_lines+1):
        if(i==1 or j==1 or i==number_lines or j==number_lines or i==j or j==number_lines-i+1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    
