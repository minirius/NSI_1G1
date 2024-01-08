import random
import os
import tkinter as tk

MOT = ""
ETAT = ""
NBR_ERREUR = 0
LISTE_DEJA_FAIT = []
WIN = False

VARIANTE = {
    'A' : 'AÀÄÂÆ',
    'C' : 'CÇ',
    'E' : 'EÉÈÊËÆŒ',
    'I' : 'IÎÏ',
    'O' : 'OÔÖŒ',
    'U' : 'UÙÜÛ'
}

def mots_longueur():
    f = open("./python/Projet2/littre.txt", encoding="UTF-8")
    count = 0
    for item in f.readlines():
        if(len(item) == len(MOT)):
            count += 1
    return count

def mots_avec_caracteres():
    f = open("./python/Projet2/littre.txt", encoding="UTF-8")
    count = 0
    TEMP = list(filter(("_").__ne__, ETAT)) 
    for item in f.readlines():
        hasAllLetters = True
        for char in TEMP:
            if not(char in item):
                hasAllLetters = False
        if hasAllLetters: count += 1
    return count

def mots_sans_caracteres():
    f = open("./python/Projet2/littre.txt", encoding="UTF-8")
    count = 0
    TEMP = list(filter(("_").__ne__, ETAT)) 
    for item in f.readlines():
        hasAllLetters = True
        for char in TEMP:
            if not(char in item):
                hasAllLetters = False
        if not hasAllLetters: count += 1
    return count

def nouvel_etat(lettre):
    global MOT, ETAT, WIN
    lettres = [lettre.upper()]
    if(VARIANTE.get(lettre) != None):
        lettres = lettres+list(VARIANTE.get(lettre))
    didModified = False
    for index, element in enumerate(MOT):
        for i in lettres:
            if(element == i):
                ETAT[index] = i
                didModified = True
    if(MOT == "".join(ETAT)):
        WIN = True
    return MOT, ETAT, didModified, WIN

def selectionner_mot():
    global MOT, ETAT
    f = open("./python/Projet2/littre.txt", encoding="UTF-8")
    MOT = random.choice(f.readlines()).strip()
    ETAT = ["_" for i in MOT]
    return MOT, ETAT

def user_input():
    lettre = input(">> ")
    if(type(lettre) != str):
        return False
    elif(len(lettre) > 1):
        return False
    return lettre

def main():
    global WIN, LISTE_DEJA_FAIT, NBR_ERREUR
    selectionner_mot()
    while (not WIN) and (NBR_ERREUR <= 8):
        print(MOT, ":", " ".join(ETAT), "Erreur: ", NBR_ERREUR)
        print("Il y a", mots_avec_caracteres(),"mot avec ce caractère")
        lettre = user_input()
        if(lettre == False): continue
        if(not nouvel_etat(lettre)[2]):
            NBR_ERREUR += 1
            LISTE_DEJA_FAIT.append(lettre)
    if(WIN): print("Gagné !")
    else: print("Perdu !")

if __name__ == "__main__":
    main()