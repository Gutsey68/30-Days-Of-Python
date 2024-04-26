import math

age = 27
height = 1.84
complex = 5 - 2j

# the area of a triangle (area = 0,5 x base x height)
triangle_base = int(input('enter the base of the triangle: '))
triangle_height = int(input('enter the height of the triangle: '))
print('The area of the triangle is ', 0.5 * triangle_base * triangle_height )

# the perimeter of a triangle (perimeter = a + b + c)
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
print('The perimeter of the triangle is ', side_a + side_b + side_c)

# area of a rectangle (area = lenght x width)
rectangle_length = int(input('Enter length: '))
rectangle_width = int(input('Enter width: '))
print('The area of the rectangle is ', rectangle_length * rectangle_width)

# the perimeter of the same rectangle ( perimeter = 2 x (length + width))
print('The perimeter of the rectangle is ', 2 * (rectangle_length + rectangle_width))

# the area of a circle (area pi x r x r)
circle_radius =  int(input('Enter the radius of the circle: '))
print('The area of the circle is ', math.pi * circle_radius * circle_radius)

#circumference of the same circle ( c = 2 x pi x r )
print('The circumference of the circle is ', 2 * math.pi * circle_radius )

# the slope, x-intercept and y-intercept of y = 2x-2
slope = 2
y_intercept = -2
x_intercept = 1

# slope is (m = y2-y1/x2-x1)
# slope between point (2, 2) and point (6,10)
slope_between = (10-2) / (6-2)

# euclidean distance between point (2, 2) and point (6,10)
euclidean_distance = math.sqrt(((10 - 6)**2) + ((2 - 2)**2))

print(slope - slope_between) # = 0

# calcul of (y = x^2 + 6x + 9)
print((-3)**2 + (6*(-3)) + 9)

# pay 
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hours: '))
print('Yout weekly earning id  is ', hours * rate_per_hour )

# number of seconds of life
number_of_years = int(input('Enter number of years you have lived: '))
print('You have lived for ', number_of_years * 60 * 60 * 24 * 365 , 'seconds' )

for i in range(1, 5 + 1):
    row = [i, 1, i, i**2, i**3]
    print(' '.join(map(str, row)))
