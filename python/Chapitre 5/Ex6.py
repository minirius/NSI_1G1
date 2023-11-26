capital = int(input("Capital: "))
duree = int(input("Durée (en année): "))
taux = int(input("Taux (en %): "))

for i in range(1, duree+1):
    capital *= 1 + taux/100

print(round(capital, 2), "€")