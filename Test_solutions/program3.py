# filters out the non-alphabetic characters and returns only the alphabetic characters.

def extract_characters(input_string):
    
    result = "" #take an empty string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            result += char
    
    return result
input_string = input("Enter the string with characters and special characters: ")
output_string = extract_characters(input_string)
print("output string with only alphabets:"+output_string)