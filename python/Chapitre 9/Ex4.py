def get_dico(file):
    return {file[i*2].strip():file[i*2+1].strip() for i in range(int(len(file)/2))}

def rechercher_numero(dico):
    nom = input("Nom >> ")
    if nom in dico.keys():
        print("-----------------------")
        print(nom, dico[nom])
        print("-----------------------")
    else:
        print("-----------------------")
        print("Introuvable")
        print("-----------------------")


def rechercher_nom(dico):
    nom = input("Nom >> ")
    dico2 = {value: key for key, value in dico.items()}
    if nom in dico2.keys():
        print("-----------------------")
        print(nom, dico2[nom])
        print("-----------------------")
    else:
        print("-----------------------")
        print("Introuvable")
        print("-----------------------")


def ajouter(file, dico):
    nom = input("Nom >> ")
    num = input('Numéro >> ')
    file.write("\n"+nom+"\n"+num)
    dico[nom] = num

if "__main__" == __name__:
    fichier = open("python\Chapitre 9\Ex4.txt", "a+")
    try:
        dico = get_dico(fichier.readlines())
        print(dico)
        while True:
            query = input("1) Rechercher Numéro\n2) Rechercher un nom\n3) Ajouter\n4) Quitter\n>> ")
            if(query == "1"):
                rechercher_numero(dico)
            elif(query == "2"):
                rechercher_nom(dico)
            elif(query == "3"):
                ajouter(fichier, dico)
            elif(query == "4"):
                break
    finally:
        fichier.close()