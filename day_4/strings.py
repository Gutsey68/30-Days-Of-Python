# concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.'
thirty = "Thirty"
days = "Days"
of = "Of"
python = "Python"
space = " "
concat = thirty + space + days + space  + of + space + python
print(concat)

# concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding_for_all = ['Coding', 'For', 'All']
print(' '.join(coding_for_all))

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper()) # change to uppercase
print(company.lower()) # change to lowercase
print(company.capitalize()) # converts the first character of the string to capital letter
print(company.title()) # return a title cased string
print(company.swapcase()) # converts uppercase to lowercase and opposite
print(company[0:6]) # slice the first word
print("Coding For All".find('Coding')) # find the first occurence of the specified value
print("Coding For All".replace("Coding", "Python")) # replace the word Coding by Python
print("Python for Everyone".replace("for Everyone", "for All"))
print('Coding For All'.split(' ')) # split the string using space as separator
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', '))
print("Coding for All".index("Coding"))
print("Coding for All".index("All")) # the last index is 11
print("Coding for All".index(" All"))

# create an acronym
def create_acronym(phrase):
    acronym=""
    words = phrase.split()
    for word in words:
        acronym += word[0].upper()
    return acronym

input_phrase = "Python For Everyone"
result = create_acronym(input_phrase)
print(result)

second_phrase = "Coding For Everyone"
second_result = create_acronym(second_phrase)
print(second_result)

# use index to determine the position of the first occurrence
print("Coding For All".index("C"))
print("Coding For All".index("F"))
print("Coding For All".rfind('l'))
print("You cannot end a sentence with because because because is a conjunction".index("because"))
print("You cannot end a sentence with because because because is a conjunction".rfind('because'))

print("You cannot end a sentence with because because because is a conjunction"[31:54])
print("You cannot end a sentence with because because because is a conjunction".find("because")) # 31

print("Coding For All".startswith('Coding')) # true
print("Coding For All".startswith('coding')) # false

print('   Coding For All      '.strip('  '))

print("30DaysOfPython".isidentifier()) # false
print("thirty_days_of_python".isidentifier()) # true

print(' #'.join([' ','Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

print('{} am enjoying this challenge. \n{} just wonder what {} next.'.format("I", "I", "is"))

print('{}     {}   {} {}\n{} {}  {} {}'.format("Name", "Age", "Country", "City", "Gauthier", 27, "France", "Colmar"))

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

x = 8
y = 6
print("{} + {} = {}".format(x, y, (x + y)))
print("{} - {} = {}".format(x, y, (x - y)))
print("{} * {} = {}".format(x, y, (x * y)))
print("{} / {} = {}".format(x, y, (x / y)))
print("{} % {} = {}".format(x, y, (x % y)))
print("{} // {} = {}".format(x, y, (x // y)))
print("{} ** {} = {}".format(x, y, (x ** y)))