#same as shopping program but modified with pincode
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = input("Enter the occupation: \n1.Student\n2. Working\nEnter any number: ")
residency = input("Are you a hosteller or a localite? \nH. Hosteller\nL. Localite\nEnter any number: ")
parent_occupation = input("Is any of your parents (or you) in armed forces or police? \nY. Yes\nN. No\nEnter any option: ")
discountPin = [100001,100023,100041,100070]
residencePin = int(input("Please enter your residence pin code:"))



if age >= 60 and gender.lower() == "m":
    print("Senior citizen discount applied, thank you for shopping")
elif age >= 45 and gender.lower() == "f":
    print("Senior citizen discount applied, thank you for shopping")
elif (age < 60 and gender.lower() == 'm') or (age <45 and gender.lower() == "f"):
    if gender.lower() == 'f':
        print("Congrats 100 voucher nyka reward is applied ")
    else:
        print("Congrats 100 voucher fastrack reward is applied")
    if(occupation =="1" and residencePin in discountPin):
        print("500 coupon on books")
    if (residency.lower() == "h" and occupation == "1"):
     print("Congrats, a 250 voucher on groceries is applied.")

if(parent_occupation.lower() == "y"):
    print("Pass to R-Day parade applied")



print("Thank you for shopping")