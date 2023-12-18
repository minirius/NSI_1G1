def chercher(string, substring):
    return substring in string

def chercherList(string, substring):
    listSubString = []
    for i in range(len(substring), len(string)):
        if string[i-3:i] == substring:
            listSubString.append((i-len(substring), i))
    return listSubString

#print(chercher("marius", "ma"))
print(chercherList("Minirinius", "ini"))