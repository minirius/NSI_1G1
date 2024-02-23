def inverse(ch:str) -> str:
    """
    Inverse permet d'inverser les lettres d'une string
    Entrée : ch<str> : une string
    Sorte : temp_liste<str> : la string ch inversée
    """
    temp_liste = list(ch)
    temp_liste.reverse()
    return "".join(temp_liste)

print(inverse("Hello"))