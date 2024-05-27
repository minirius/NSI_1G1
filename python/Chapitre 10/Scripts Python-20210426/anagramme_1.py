def anagramme(chaine1,chaine2):
    assert type(chaine1) == str and type(chaine2) == str, "Les deux paramètres en entrée doivent être des chaines de caractères"
    assert len(chaine1) > 0 and len(chaine2) > 0, "Les deux chaines de caractères entrées sont non vides"
    if len(chaine1) == len(chaine2):
         for car in chaine1:
            if car not in chaine2:
                return False
         for car in chaine2:
              if car not in chaine1:
                return False
         return True
    else:
        return False

