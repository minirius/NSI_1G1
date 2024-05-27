def occurence_lettre(string):
    occurence = {}
    string = string.lower()
    lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for lettre in lettres:
        occurence[lettre] = string.count(lettre)
    return occurence

print(occurence_lettre("Salut, ajujourdh'ui je vais vous manger"))