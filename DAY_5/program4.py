'''Write an algorithm to output 1 if the word? is a right rotation of word2 otherwise output -1.
Input
The first line of the input consists of a string - word?, representing the first word
The second line consists of a string word2, a string representing the second word.
Output
Print 1 if the word is a right rotation of word2 otherwise print -1'''

original_str=input("Enter the original string")
rtl_string=input("Enter the rotational string")
temp_str=rtl_string*2
if (temp_str.find(original_str) != -1):
    print(f'{rtl_string} is rotated string')
else:
    print(f'{rtl_string} is not a rotated string')

