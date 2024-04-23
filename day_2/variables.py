import math

# Day 2: 30 Days of python programming

# personal information and hobbies
first_name = 'gauthier'
last_name = 'seyzeriat--meyer'
full_name = first_name + ' ' + last_name
country = 'france'
city = 'colmar'
age = 27
current_year = 2024
is_married = False
is_true = True
is_light_on = True
car, sport, pet, height = 'polo', 'bodybuilding', 'cat', 184 

# type checks
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(current_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(car))
print(type(sport))
print(type(pet))
print(type(height))

# length checks
print(len(first_name))
print(len(last_name) - len(first_name))

# basic arithmetic operations
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two 
exp = num_one ** num_two
floor_division = num_one // num_two

# calculation of the area of a circle (radius is 30 meters)
radius = 30

# area of a circle a = πr^2
area_of_circle =  math.pi * (radius**2)
print("L'aire du cercle de rayon", radius, "mètres est", area_of_circle, "mètres carrés.")

# calculation of the circumference of a circle c = 2πR

circum_of_circle = 2 * math.pi * 30
# calculation of the area with user input
user_number = int(input('Entrez un nombre: '))
area_of_user = math.pi * (user_number**2)

# user personal information input
user_first_name = input('Entrez votre prénom: ')
user_last_name = input('Entrez votre nom de famille: ')
user_country = input('Entrez votre pays: ')
user_age = int(input('Entrez votre age: '))

# display help on python keywords
help('keywords')

"""

Here is a list of the Python keywords.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

"""