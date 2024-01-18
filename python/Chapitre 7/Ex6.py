stop = False
listeNote = []
while not stop:
    if(listeNote != []):
        listeNote.sort()
        moyenne = 0
        print("---------------")
        for e in listeNote: 
            print(e, end=" ")
            moyenne += e
        print();moyenne = moyenne / len(listeNote)
        print("Pire:", listeNote[0],"Meilleur:", listeNote[-1],"Moyenne", moyenne)
        print("---------------")

    nbr = int(input("Note : "))
    if(nbr >= 0):
        listeNote.append(nbr)
    else:
        stop = True

