import math 
N=int(input("Enter the n value"))
prime = True # assume the number N is Prime
for i in range(2,math.ceil(math.sqrt(N)+1)):
	if N % i == 0:
		print(f"{N }is not Prime number")
		prime = False
		break 
if prime:
	print(f"{N} is a Prime number")