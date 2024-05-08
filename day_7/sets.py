# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Salesforce', 'SAP', 'Cisco Systems', 'Dell Technologies'])
it_companies.pop

'''
The discard() method removes the specified item from the set. 
This method is different from the remove() method, 
because the remove() method will raise an error if the specified item does not exist, 
and the discard() method will not
'''

C = A.union(B) # join A and B
A.intersection(B) # find A intersection B
A.issubset(B) # is A subset to B : True
A.isdisjoint(B) # are A and B disjoint sets : False
A.update(B) # join A with B
B.update(A) # join B with A

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

B.symmetric_difference(A) # the symmetric difference between A and B is {27, 28}
del A
del B

set_age = set(age)
print(len(set_age))
print(set_age)
print(len(age))
print(age) # the list is bigger 

'''
In Python, a string is an immutable sequence of characters used for text representation, 
a list is a mutable collection of ordered elements, a tuple is an immutable version of a list, 
and a set is an unordered collection of unique elements. 
While strings, lists, and tuples allow indexing, sets do not. 
Lists and sets are mutable, enabling modification, whereas strings and tuples are immutable, 
meaning their contents cannot be changed after creation.
'''

phrase = 'I am a teacher and I love to inspire and teach people'

# convert string to list
def Convert(string):
    li = list(string.split(" "))
    return li

set_phrase = set(Convert(phrase))
print(len(set_phrase)) # 10 words