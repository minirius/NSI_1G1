def invert(dico):
    return {value: key for key, value in dico.items()}

couleur = {"black":"noir", "red":"rouge", "vert":"green", "blue":"bleu", "yellow":"jaune", "violet":"purple"}
print(invert(couleur))