def anne_bissextile(annee: int) -> bool:
    assert type(annee) == int, "Année doit etre un nombre entier"
    assert annee >= 0, "Année doit être un nombre négatif entier positif"

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        return True
    else:
        return False

if "__main__" == __name__:
    print(anne_bissextile(2024))