def cesar(string, cle):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    finalString = ""
    for element in string:
        if element == " ":
            finalString += " "
        else:
            finalString += ALPHABET[(ALPHABET.find(element.lower())+cle) % (len(ALPHABET)-1)]
    return finalString

print(cesar("Marius Nerantzakis", 5))