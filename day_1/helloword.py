# check the python version 

import math
import sys
print(sys.version)

# operations

print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

# strings

print('Gauthier')
print('Seyzeriat')
print('France')
print('I am enjoying 30 days of python')

# data types 

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneth','Python','Finland']))
print(type('Gauthier'))
print(type('Seyzeriat'))
print(type('france'))

# Example data types
print("Integer example:", 8)  # integer
print("Float example:", 7.4)  # float
print("Complex number example:", 2 + 4j)  # complex
print("String example:", 'hello world')  # string
print("Boolean example:", True)  # boolean
print("List example:", [1, 5, 3])  # list
print("Tuple example:", ('push', 'pull', 'legs'))  # tuple
print("Set example:", {1, 3, 7, 9})  # set
print("Dictionary example:", {'name': 'gauthier', 'age': 27, 'location': 'alsace'})  # dictionary

# Euclidean distance between (2, 3) and (10, 8)

# d(p,q)^2 = (q1-p1)^2 + (q2-p2)^2

distance = math.sqrt(((10 - 2)**2) + ((8 - 3)**2))
print("Euclidean distance between (2, 3) and (10, 8) is:", distance)

len('python') == len('dragon')
print('on' in 'python')
print('on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in ('dragon' or 'python'))
print(str(float(len('python'))))

# if number % 2 == 0 , number is even

print(7//3) # = 2
print(int(2.7)) # = 2, both results are equal

type('10') # str
type(10) # int , not equal

int('9.8') # error 
