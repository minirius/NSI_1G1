def safeInt(nbr):
    if(nbr.isdigit()):
        return int(nbr)
    else:
        print("Votre nombre n'est pas valide")
        exit()

def safeFloat(nbr):
    if(nbr.isdigit()):
        return float(nbr)
    else:
        print("Votre nombre n'est pas valide")
        exit()