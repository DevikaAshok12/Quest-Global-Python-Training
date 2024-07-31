mark=int(input("Enter the mark :"))
if 91<=mark and mark<=100:
    print("Distinction")
elif 75<=mark and mark<=90:
    print("First Class")
elif 50<=mark and mark<=74:
    print("Second Class")
elif 0<=mark and mark<=49:
    print("Failed")
else:
    print("Enter a valid choice")