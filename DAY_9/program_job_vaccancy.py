#job vaccancy program
branches = {1: 'ECE', 2: 'Mech', 3: 'BCOM'}
preferences = {1: 'Maths', 2: 'English', 3: 'Art'}
name=input("Enter your name :")
branch_input = input("Enter your branch--\n1. for ECE 2. for Mech 3. for BCOM: ")
try:
    branch = branches.get(int(branch_input), "Invalid Branch")
    if branch == "Invalid Branch":
        raise ValueError("Invalid Branch")
except ValueError:
    print("Please provide a valid branch input.")
    exit(1)

preference_input = input("Enter your preferences (1 for Maths, 2 for English, 3 for Art) separated by commas: ")
try:
    preference_list = list(map(int, preference_input.split(',')))
    if not (1 <= len(preference_list) <= 3):
        raise ValueError("Invalid Preference numbers")
except ValueError:
    print("Please provide valid preference inputs.")
    exit(1)

marks_input = input("Enter your marks for Maths, English, and Art separated by commas: ")
try:
    marks = list(map(int, marks_input.split(',')))
    if len(marks) != 3:
        raise ValueError("Please enter exactly three marks.")
except ValueError:
    print("Please provide valid marks inputs.")
    exit(1)

pass_mark = 1
for i in marks:
    if(i<35):
        pass_mark=0
        break

maths, english, art = marks
eligible = False
for pref in preference_list:
    if branch == "ECE" and pass_mark and art > 90 and english > 90:
        if pref == 3 or pref == 2:
            print("Eligible for Marketing")
            eligible = True
            break;
    elif branch == "BCOM" and pass_mark and maths > 95:
        if pref == 1:
            print("Eligible for Accounts")
            eligible = True
            break;
    elif branch == "Mech" and pass_mark and maths > 90 and english > 90:
        if pref == 1 or pref == 2:
            print("Eligible for Sales")
            eligible = True
            break;

if eligible == 0 :
    print("No openings for provided criteria")

'''pass marks is 35

Marketing (ECE): Art>90 + Literature>90, pass in all subject (maths > 35)

Accounts (BCOM): Maths>95, pass in all subject (English and Arts > 35)

Sales (MECH): Maths>90 + Literature>90, pass in all subject (Art > 35)
'''