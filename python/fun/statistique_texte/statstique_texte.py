import os
import random

def get_letter_probability(texte):
    list_texte = list(texte.lower())
    MAIN_DICT = {}
    for i, e in enumerate(list_texte):
        if(i==0): MAIN_DICT[e] = {}
        elif e == '�' or list_texte[i-1] == "�": continue
        else:
            if e in MAIN_DICT[list_texte[i-1]]:
                MAIN_DICT[list_texte[i-1]][e] += 1
            else:
                MAIN_DICT[list_texte[i-1]][e] = 1
            if not(e in MAIN_DICT):
                MAIN_DICT[e] = {}
    return MAIN_DICT

def more_child_letter(liste):
    childName = ""
    childNum = 0
    for i, e in enumerate(liste):
        if childNum < len(liste[e]) and e != " ":
            print(e, len(liste[e]))
            childNum = len(liste[e])
            childName = e
    return childName

def get_next_letter(liste, lettre):
    maxLetter = ""
    maxNum = 0
    for e in liste[lettre]:
        if maxNum < liste[lettre][e] and random.randint(0, 10) < 5:
            maxLetter = e
            maxNum = liste[lettre][e]
    return maxLetter

if(__name__ == "__main__"):
    os.chdir(os.getcwd()+'/python/fun/statistique_texte')
    texte = open("livre1.txt", mode='r', encoding='UTF-8')
    proba = get_letter_probability(texte.read())
    phrase = "Je disais souvent "
    for i in range(500):
        phrase += get_next_letter(proba, phrase[-1])
    print(phrase)