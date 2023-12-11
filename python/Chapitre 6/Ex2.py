nom = input("Votre nom : ")
listNom = nom.split(" ")
listInitiale = []
for element in listNom:
    listInitiale.append(element[0].upper())
print(".".join(listInitiale))