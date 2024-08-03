#find maximum possible total sum of values in all cells he can visit on his path
row_of_matrix = int(input("Enter the number of rows of matrix :"))
column_of_matrix=2
matrix = []

for i in range(row_of_matrix):
    print(f'Enter {column_of_matrix} numbers of Row-{i+1}')
    row_numbers = [] # List that stores numbers of a specific row
    for j in range(column_of_matrix): # To read numbers of a row
        row_numbers.append(int(input()))
    matrix.append(row_numbers)
print("Matrix  is:")
 
for row in matrix:
    for number in row:
        print('%5s'%(number), end='')
    print()
sum_of_max_elements = max(matrix[0])
previous_max_element = max(matrix[0])
 
for i in range(1,len(matrix)):
    current_max_element = max(matrix[i])
    if current_max_element > previous_max_element:
        sum_of_max_elements += current_max_element
        previous_element = current_max_element
    else:
        break
print("The maximum possible sum of values in all the cells he can visit is = ",sum_of_max_elements)