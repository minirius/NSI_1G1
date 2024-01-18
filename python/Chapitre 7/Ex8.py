import random

def hasard_liste(n):
    return [random.randint(0, 1000) for i in range(n)]

def is_500(liste):
    return 500 in liste

def croissant(n):
    return [i for i in range(n)]

liste = hasard_liste(500)
print(liste)
print(is_500(liste))
print(croissant(500))