def occurences(t):
    returnlist = {}
    for i in t:
        if i in returnlist:
            returnlist[i] += 1
        else:
            returnlist[i] = 1
    return returnlist

def get_book():
    fichier = open("python\Chapitre 9\ltdme80j.txt", "r+", encoding='utf-8')
    final = fichier.read().split()
    fichier.close()
    return final

def plus_frequent(d, k):
    temp_dict = {}
    for key, value in d.items():
        if(len(key) == k):
            temp_dict[key] = value
    max_mot = ""
    max_occu = 0
    for key, value in temp_dict.items():
        if(value > max_occu):
            max_mot = key
            max_occu = value

    return max_mot, max_occu

def compare_tableau(tab1, tab2):
    return tab1 == tab2

contenu = get_book()
occu = occurences(contenu)

print(plus_frequent(occu, 15))
print(compare_tableau({"hello":0, "main":5, "cac40":20}, {"hello":0, "main":5, "cac40":20, "cac44":80}))