import random
from random import randint


#names = ['Juan', 'Laura' ,'Maria','Pedro', 
#            'Jesus', 'Emilio', 'Nicolas', 'Marcos', 
#            'Ricardo', 'Ignacio', 'Rodrigo', 'Joaqquin', 
#            'Manuel', 'Rocio', 'Mercedes', 'Flor']

def simple(names):
    result = [{'name':random.choice(names), 'age':randint(1,100)} for i in range(10)]
    return result

def order(listnames: list):
    return sorted(listnames, key=lambda age:age['age'])
