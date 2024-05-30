def insere (t ,i ,v):
    j = i
    while j > 0 and t[j -1] > v:
        t[j] = t[j - 1]
        j = j - 1
    t[j] = v
    return t

def tri_par_insertion (t ):
    for i in range (1 , len (t)):
        insere (t ,i ,t [i ])
    return t

def freq(tableau):
    most_freq = {}
    most_freq_couple = (0, 0)

    for e in tableau:
        if e in most_freq.keys():
            most_freq[e] = most_freq[e] + 1
        else:
            most_freq[e] = 1

        if(most_freq[e] > most_freq_couple[1]):
            most_freq_couple = (e, most_freq[e])

    return most_freq_couple

##### MAIN ######
Tableau = [3 ,4 ,1 ,7 ,2]
print (Tableau)
print (tri_par_insertion(Tableau))
Tab = [0, 3, 4, 5, 2, 7, 6, 8, 4, 9, 6, 0, 4, 6, 7, 3, 1, 2, 8, 9, 4, 5, 6, 2, 0, 6]
print(freq(Tab))