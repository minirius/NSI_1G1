import random

def texte_tranforme(text):
    listText = text.split(" ")
    listFinal=[]
    for word in listText:
        if(len(word) >= 4):
            listWord = []
            for i in word[1:-1]:
                listWord.append(i)
            random.shuffle(listWord)
            newWord = word[0] + "".join(listWord)+ word[-1]
            listFinal.append(newWord)
        else:
            listFinal.append(word)
    return " ".join(listFinal)

print(texte_tranforme("Bonjour je pense que l'homme est un animal très bouleversant pour son environnement"))