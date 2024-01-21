import os
import random

FILE_NAME = "balzac.txt"

def get_world_probability(texte):
    list_texte = texte.lower().split(" ")
    MAIN_DICT = {}
    for i, e in enumerate(list_texte):
        if(i==0): MAIN_DICT[e] = {}
        elif e == '�' or list_texte[i-1] == "�" or e=="" or list_texte[i-1] == "": continue
        else:
            if e in MAIN_DICT[list_texte[i-1]]:
                MAIN_DICT[list_texte[i-1]][e] += 1
            else:
                MAIN_DICT[list_texte[i-1]][e] = 1
            if not(e in MAIN_DICT):
                MAIN_DICT[e] = {}
    return MAIN_DICT

def get_next_world(liste, mot):
    maxLetter = ""
    maxNum = 0
    for e in liste[mot]:
        if maxNum < liste[mot][e] and random.randint(0, 10) < 5:
            maxLetter = e
            maxNum = liste[mot][e]
    return maxLetter

def save_data(data):
    file = open(FILE_NAME+".learned", "w", encoding='UTF-8') 
    file.write(str(data)) 
    file.close() 

def search_data():
    proba = []
    if(os.path.exists(FILE_NAME+".learned")):
        file = open(FILE_NAME+".learned", "r", encoding='UTF-8') 
        proba = eval(file.read())
        file.close()
        return proba
    else:
        return {}
    
if(__name__ == "__main__"):
    os.chdir(os.getcwd()+'/python/fun/statistique_texte')
    texte = open("train_mot/"+FILE_NAME, mode='r', encoding='UTF-8')
    if(search_data() == {}):
        proba = get_world_probability(texte.read())
        print("Working...")
    else:
        proba = search_data()
        print("Reading File...")
    print("Done.")
    save_data(proba)
    phrase = list(proba)[random.randint(0, len(proba)-5)]
    for i in range(50):
        phrase += " "+get_next_world(proba, phrase.split(" ")[-1])
    print(phrase)