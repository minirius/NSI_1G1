dico = {
    "Bidouille":["Maths", "Physique-Chimie", "NSI"], 
    "Thomas":["Maths", "Physique-Chimie", "NSI"], 
    "Marius": ["Maths", "Physique-Chimie", "NSI"]
}

def add_eleve(nom, matieres):
    dico[nom] = matieres

def supp_eleve(nom):
    dico.pop(nom)

def update_terminal(nom, abandonne):
    nouvelles_matieres = []
    for matiere in dico[nom]:
        if matiere == abandonne:
            nouvelles_matieres.append("Abandonné")
        else:
            nouvelles_matieres.append(matiere)
    dico[nom] = nouvelles_matieres

def afficher_dico():
    print("Nom             Matières")
    for key, values in dico.items():
        print(key.ljust(15), ", ".join(values))
    
supp_eleve("Bidouille")
update_terminal("Thomas", "Maths")
afficher_dico()
