ch = input("Enter a letter: ")

if ch.isalpha():
    ch = ch.lower()  
    if ch in 'aeiou':
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Please enter a single alphabetic character.")