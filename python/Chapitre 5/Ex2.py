import math

def roundSup(n):
    if(round(n) == n):
        return n
    else:
        return (round(n)+1)

def diviseurs(nbr):
    maxNum = roundSup(math.sqrt(nbr))
    diviseur = set([])

    for i in range(1, maxNum+1):
        if(nbr%i == 0): diviseur.add(i);diviseur.add(nbr//i)

    return sorted(diviseur)

print(diviseurs(1506))