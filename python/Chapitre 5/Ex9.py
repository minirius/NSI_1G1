n = 100

def nombreTriplets(n=100):
    n+=1
    liste = []

    for a in range(n):
        for b in range(n):
            for c in range(n):
                if((1 <= a and a <= b and b <= c and c <= 100) and (a**2 + b**2 == c**2)):
                    liste.append((a, b, c))
    return liste

result = nombreTriplets(100)
print(result, len(result))
