myString = input(">> ")
nbr = 0
for char in myString:
    if(char.lower() == "z"): nbr += 1

print("Il y a", nbr, "lettres z dans", myString)