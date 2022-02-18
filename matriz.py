from random import randint

n = 10
def matriz(n):
    return [([(randint(1, n)) for x in range(5)]) for y in range(5)]
    