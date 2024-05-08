dog = {}
dog = {
    'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Golden Retriever',
    'legs': 4,
    'age': 3
}

student = {
    'first_name' : 'Gauthier',
    'last_name' : 'Seyzeriat--Meyer',
    'gender' : 'mâle',
    'age' : 27,
    'marital status' : 'single',
    'skills' : ['JavaScript', 'React', 'Python'],
    'country' : 'France',
    'city' : 'Colmar',
    'adresse' : '30 rue du kebab'
}

print(len(student)) # 9
print(student['skills'])
print(type(student['skills']))
student['skills'] = ['JavaScript', 'React', 'Python', 'Node', 'MySQL']
print(student.keys())
print(student.values())
print(student.items())

del student['adresse']
del student