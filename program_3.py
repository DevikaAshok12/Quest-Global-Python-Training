import math
number = int(input("Enter a number: "))
root = math.isqrt(number)
int_root=math.floor(root)
if int_root*int_root ==number:
    print("prefect square")
else:
    print("Not perfect square")
