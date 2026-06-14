# OOPS - object oriented programming language

# creating a class and a blueprint
class Student:
    def __init__(self, name, age):
            self.name = name
            self.age = age

# taking input
name = input('ENTER NAME : ')
age = int(input('ENTER AGE : '))

# creaing object
s1 = Student(name, age)     # in the parameter values are assigned automatically

print(f'The name is {s1.name} and the age is {s1.age}')

print('***********************************************************************')


class person:
      def __init__(self, name, age, height, location):
            self.name = name
            self.age = age
            self.height = height
            self.location = location


name = input('NAME: ')
age = int(input('AGE: '))
height = float(input('HEIGHT: '))
location = input('LOCATION: ')

p1 = person(name, age, height, location)

print(f"""
    NAME : {p1.name}
    AGE : {p1.age}
    HEIGHT : {p1.height}
    LOCATION : {p1.location}
""")