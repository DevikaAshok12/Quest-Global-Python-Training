'''
* Name

* Age
 
15% discount for all product for senior citizen
 
* Gender

male senior citizen (60 and above)

female senior citizen (45 and above)
 
100 rupees nyka, fastrack, if female (<45)

100 coupon on titan, fastrack, if male (<60)

----
 
*Occupation: Working, Student (PIN code should be local)
 
College: 500 coupon on books

Working: NA
 
----

*Residence: Hosteller, Localite (Hostel name should be valid)
 
Hosteller: Groceries

Localite: NA
 
----

* Armed Forces: Yes/No (Check from external file)
 
Yes: Free pass for R-day parade for 2

No: Na
 

 '''
age = int(input("Enter age: "))
gender = input("Enter gender: \nM. Male\nF. Female\nO. Other\nEnter any number.")
occupation = input("Enter the occupation: \n1.Student\n2. Working\nEnter any number: ")
residency = input("Are you a hosteller or a localite? \nH. Hosteller\nL. Localite\nEnter any number: ")
parent_occupation = input("Is any of your parents (or you) in armed forces or police? \nY. Yes\nN. No\nEnter any option: ")




if age >= 60 and gender.lower() == "m":
    print("Senior citizen discount applied, thank you for shopping")
elif age >= 45 and gender.lower() == "f":
    print("Senior citizen discount applied, thank you for shopping")
elif (age < 60 and gender.lower() == 'm') or (age <45 and gender.lower() == "f"):
    if gender.lower() == 'f':
        print("Congrats 100 voucher nyka reward is applied ")
    else:
        print("Congrats 100 voucher fastrack reward is applied")
    if(occupation =="1"):
        print("500 coupon on books")
    if (residency.lower() == "h" and occupation == "1"):
     print("Congrats, a 250 voucher on groceries is applied.")

if(parent_occupation.lower() == "y"):
    print("Pass to R-Day parade applied")



print("Thank you for shopping")