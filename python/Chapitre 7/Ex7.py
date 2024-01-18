notes = [12, 7, 6, 5, 8, 14, 13, 7, 5, 8]

def somme(liste):
    sommeliste = 0
    for e in liste: sommeliste+=e
    return sommeliste

def moyenne(liste):
    return somme(liste) / len(liste)

def dessus_dessous_moyenne(liste):
    return [e for e in liste if e>10], [e for e in liste if e<10]

print(somme(notes))
print(moyenne(notes))
dessus, dessous = dessus_dessous_moyenne(notes)
print(dessus, dessous)
print(moyenne(dessus), moyenne(dessous))