squares = []
for i in range(10):
    squares.append(i * i)
print('Squares = ', squares)

#List Comprehension
[x**2 for x in range(10)]
 
'''step1: [ ]
We are saying, we need a list
 
step2: x ** 2
elements of the list will be x ** 2
 
step3: for x in range(10)
values for x will be supplied from the for loop
-----------------------------'''
squares2 = [x**2 for x in range(10)]
print('Squares2 = ', squares2)

#Using Map and Lambda Function:
 
squares3 = list(map(lambda x: x**2, range(10)))
print('Squares3 = ', squares3)
