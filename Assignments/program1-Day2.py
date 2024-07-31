#Find sum of Even placed digits in a number

number= input("Enter a number: ") # Read input from user
sum_even = 0
for i in range(1, len(number), 2):
    sum_even += int(number[i])
print(f'sum of even placed digit in {number}is {sum_even}')