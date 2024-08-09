class Person:
    def __init__(self, age, gender, residency,occupation):
        self.age = age
        self.gender = gender
        self.residency = residency
        self.occupation = occupation
    def senior(self):
        if (self.age > 60 and self.gender == 'm') or (self.age > 45 and self.gender == 'f'):
            print("Senior citizen discount of 15 percent applied")
    def discount_for_male_female(self):
        if (self.age < 60 and self.gender == 'm') or (self.age < 45 and self.gender == 'f'):
            if self.gender == 'm':
                print("Congrats! A 100 voucher for Fastrack is applied.")
            else:
                print("Congrats! A 100 voucher for Nykaa is applied.")
class Student(Person):
    def __init__(self, age, gender, residency, occupation, residence_pin, discount_pin):
        super().__init__(age, gender, residency, occupation)
        self.residence_pin = residence_pin
        self.discount_pin = discount_pin
        if self.residence_pin in self.discount_pin:
            print("500 coupon on books is applied.")
        if self.residency == 'h':
            print("Congrats, a 250 voucher on groceries is applied.")
class Working(Person):
    def __init__(self, age, gender, residency, occupation, office_pin):
        super().__init__(age, gender, residency, occupation)
        self.office_pin = office_pin

gender_dict = {1: 'm', 2: 'f'}
residency_dict = {1: 'h', 2: 'l'}
occupation_dict = {1: 'Student', 2: 'Working'}
discount_pin = [100001, 100023, 100041, 100070]

try:
    age = int(input("Enter your age: "))
    gender_key = int(input("Select your gender \n1: Male \n2: Female\nEnter any number: "))
    if gender_key not in gender_dict:
        raise ValueError
    occupation_key = int(input("Choose from options \n1: Student \n2: Working\nEnter any number: "))
    if occupation_key not in occupation_dict:
        raise ValueError
    residency_key = int(input("Select your residence \n1: Hosteller \n2: Localite\nEnter any number: "))
    if residency_key not in residency_dict:
        raise ValueError
    pin_code = int(input("Please enter your pin code: "))

    person = Person(age, gender_dict[gender_key], residency_dict[residency_key],occupation_dict[occupation_key])
    person.senior()
    if occupation_key == 1:  # Student
        student = Student(age, gender_dict[gender_key], residency_dict[residency_key], occupation_dict[occupation_key], pin_code, discount_pin)
        student.discount_for_male_female()
    elif occupation_key == 2:  # Working
        employee = Working(age, gender_dict[gender_key], residency_dict[residency_key], occupation_dict[occupation_key], pin_code)
        employee.discount_for_male_female()
    print("Thank you for shopping!")

except ValueError:
    print("Please enter a valid choice.")