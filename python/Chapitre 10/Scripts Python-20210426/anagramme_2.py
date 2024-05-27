def anagramme(chaine1, chaine2):
    """
    Cette fonction permet de 
    """
    assert type(chaine1) == str and type(chaine2) == str, "Les deux paramètres en entrée doivent être des chaines de caractères"
    assert len(chaine1) > 0 and len(chaine2) > 0, "Les deux chaines de caractères entrées sont non vides"
    
    if len(chaine1)==len(chaine2): 
        for car in chaine1: 
            if car not in chaine2:
                return False
            else:
                if chaine2.index(car)==len(chaine2): 
                    chaine2=chaine2[:len(chaine2)-1]
                    chaine2=chaine2[:chaine2.index(car)]+chaine2[chaine2.index(car)+1:]
        return True
    else:
        return False