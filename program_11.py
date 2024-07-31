input_number = int(input('Enter a number to count number of odd digits in it: '))
 
sum_of_digits = 0
temp_number = input_number
 
while temp_number != 0:
    digit=temp_number%10
    sum_of_digits += digit
    temp_number = temp_number // 10
    
 
print(f'sum of digits in {input_number} is {sum_of_digits}')