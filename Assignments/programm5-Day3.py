#different ways of adding elements to a list
#append
squares = []
for i in range(10):
    squares.append(i * i)
print('Squares = ', squares)

#List Comprehension
my_list = [1, 2, 3]
my_list = [x for x in my_list] + [4, 5]
print(my_list)

#Using Map and Lambda Function:
squares3 = list(map(lambda x: x**2, range(10)))
print('Squares3 = ', squares3)

#using list concatenation
my_list = [1, 2, 3]
my_list = my_list + [4, 5]
print(my_list) 

#using insert
my_list = [1, 2, 3]
my_list.insert(1, 1.5)  # Insert 1.5 at index 1
print(my_list)

#different ways of remove elements to a list
#using remove
my_list = [1, 2, 3, 4]
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)

#using pop
my_list = [1, 2, 3, 4]
element = my_list.pop()  # Removes and returns the last item
print(element)  
print(my_list)

#using del
my_list = [1, 2, 3, 4]
del my_list[1]  # Deletes the item at index 1
print(my_list)

#using List Comprehension
my_list = [1, 2, 3, 4, 5]
my_list = [x for x in my_list if x % 2 == 0]  # Keeps only even numbers
print(my_list) 

#using clear
my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)

#using slice
my_list = [1, 2, 3, 4, 5]
my_list = my_list[:2] + my_list[3:]  # Removes the item at index 2
print(my_list)