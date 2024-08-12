class Eatable:
    def __init__(self, carbs, fat, protein):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein
        def describe(self):
        return f"Carbs: {self.carbs}g, Fat: {self.fat}g, Protein: {self.protein}g"

        
       
class Vegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isPeelable):
        super().__init__(carbs, fat, protein)
        self.isPeelable = isPeelable
        def describe(self):

class NonVegetarian(Eatable):
    def __init__(self, carbs, fat, protein, isBoneless):
        super().__init__(carbs, fat, protein)
        self.isBoneless = isBoneless
        def describe(self):
        
food_item_dict = {1: 'Vegetarian', 2: 'NonVegetarian'}
peelable_dict = {1: True, 2: False}
bonless_dict = {1: True, 2: False}
carbs = int(input("Enter the amount of carbs: "))
fat = int(input("Enter the amount of fat : "))
protein = int(input("Enter the amount of protein : "))
