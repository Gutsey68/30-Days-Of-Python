empty_tuple = ()
brothers_tuple = ('matthieu', 'guillaume')
sisters_tuple = ('aude', 'luna')
siblings = brothers_tuple + sisters_tuple # 4 siblings
family_members = ('marie-odile', 'serge') + siblings
print(family_members)

parents = family_members[0:2]
brothers = family_members[2:4]
sisters = family_members[4:6]
print(parents, brothers, sisters)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('kibble', 'canned food', 'raw diet', 'freeze-dried treets')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp)

middle_item = food_stuff_lt[6:7]
print('middle item : ' , middle_item)

three_first_items = food_stuff_lt[0:3]
three_last_items = food_stuff_lt[9:12]
print('3 first items : ', three_first_items , '3 last items : ' , three_last_items)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)