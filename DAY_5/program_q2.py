#sort the arrays in non-increasing order
def sort_array(test_cases):
    for arrays in test_cases:
        arrays.sort(reverse=True)

number_of_testcase = int(input("Enter the number of test cases: "))  
test_cases = []
for i in range(number_of_testcase):
    size = int(input("Enter the size of array:")) 
    array = list(map(int, input(f'Enter array {i+1} elements:').split()))  
    test_cases.append((array))

#print(test_cases)
sort_array(test_cases)
print("Arrays Sorted in descending order :")
for i in test_cases:
    print(" ".join(map(str, i))) 
