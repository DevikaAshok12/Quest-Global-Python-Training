#Global methods and keywords:
numbers = [1, 2, 3, 4, 5]
del numbers[1:3]
print(numbers) # [1, 4, 5]
del numbers[1]
print(numbers) # [1, 5]
del numbers[:] # we are deleting all the elements from the list
print(numbers) # []
numbers.insert(10, 0) # inserting the element 10 at index 0
 
#INSERT ELEMENT AT REAR OF THE LIST: 3 different ways
a=[1,7,8]
print(a)
x=20
a.insert(len(a), x)
a.append(x)
print(a)
element=[5]
a[len(a):] = [element]
print(a)
 
#Below is an error
#numbers[len(numbers):] = 3
#TypeError because we must assign only a list(itarable) not a primitive value