class Person:
    def __init__(self, age, gender, pincode):
        self.age = age
        self.gender = gender
        self.pincode = pincode

class Student(Person):
    def __init__(self, age, gender, pincode, residence):
        super().__init__(age, gender, pincode)
        self.residence = residence
    def __init__(self, age, gender, pincode, residence, isquota):
        super().__init__(age, gender, pincode)
        self.residence = residence
        print("Sports quota")
class Employee(Person):
    def __init__(self, age, gender, pincode):
        super().__init__(age, gender, pincode)
#student1 =Student("25","female",121100,"H")
student2 =Student("25","female",121100,"H",True)

