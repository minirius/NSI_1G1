nombre_to_lettre = {1:"un", 2:"deux", 3:"trois", 4:"quatre", 5:"cinq", 6:"six", 7:"sept", 8:"huit", 9:"neuf"}
phrase = input(">> ")

def modifier(string):
    for nbr, nom in nombre_to_lettre.items(): 
        string = string.replace(str(nbr), nom)

    return string

print(modifier(phrase))