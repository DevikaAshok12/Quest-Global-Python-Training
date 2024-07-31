#Accept the food type (veg or non-veg) from the user and then prompt her for the food item number and serve her the food.
 
food_items1 = {
    1 : 'Mysuru Filter Coffee',
    2 : 'Yummy Idly-vada',
    3 : 'Worlds soft Mysuru Mailari Dosa',
    4 : 'Bhupal Special Poha',
    5 : 'Bengaluru tamato-peanuts Upama'
}
food_items2 = {
    1 : 'Chicken Biriyani',
    2 : 'Chicken Noodles',
    3 : 'Chineese Egg Fried Rice',
    4 : 'Chicken Fried Rice',
    5 : 'Mutton soup'
}
print('Welcome to our hotel Rameshwaram Cafe')
print('1.Veg\n2.Non Veg')
food_option_number = int(input('Enter the type of food item number that you wish:'))

if food_option_number==1:
  print('1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama')
  food_item_number = int(input('Enter the food item number that you wish:'))
  if food_item_number < 1 or food_item_number > 5:
    print('Invalid choice entered')
  else:
    print('Your ' + food_items1.get(food_item_number) + ' is here')
elif food_option_number==2:
  print('1:Biriyani 2:Noodles 3:Egg fried rice 4:Chicken Fried rice 5:Mutton soup')
  food_item_number = int(input('Enter the food item number that you wish:'))
  if food_item_number < 1 or food_item_number > 5:
    print('Invalid choice entered')
  else:
    print('Your ' + food_items2.get(food_item_number) + ' is here')
else:
  print("Enter a valid choice ")
  
print('Thank you, Visit again')

