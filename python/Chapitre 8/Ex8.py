def bissextile(year:int) -> bool:
    """
    Bissextile est une fontion qui permet de trouver les années bissextile
    Entrée : year<int> → L'année
    Sorte : <bool> → Si l'année est bissextile
    """
    if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return True
    return False

def nbJoursAnnee(a:int) -> int:
    """
    nbJoursAnnee renvoie le nombre de jour dans une année
    Entrée : a<int> → L'année
    Sorte : <int> → nbr de jour
    """
    return 366 if bissextile(a) else 365

def nbJoursMois(a:int, m:int) -> int:
    """
    nbJoursAnnee renvoie le nombre de jour dans un mois selon l'année
    Entrée : a<int> → L'année
             m<int> → Le mois
    Sorte : <int> → nbr de jour
    """
    if(m == 1 or m== 3 or m==5 or m==7 or m==8 or m==10 or m==12):
        return 31
    elif(m==4 or m==6 or m==9 or m==11):
        return 30
    elif(m==2):
        return 29 if bissextile(a) else 28

def nbJours(j1:int, m1:int, a1:int, j2:int, m2:int, a2:int) -> int:
    """
    nbJours renvoie le nombre de jour entre deux dates
    Entrée : j1<int> → Le jour de la date 1
             m1<int> → Le mois de la date 1
             a1<int> → L'année de la date 1
             j2<int> → Le jour de la date 2
             m2<int> → Le mois de la date 2
             a2<int> → L'année de la date 2
    Sorte : <int> → nbr de jour
    """
    j = j2-j1
    a = a1
    while a < a2:
        j += nbJoursAnnee(a)
        a+=1
    m = m1
    while m < m2:
        j += nbJoursMois(a2, m)
        m+=1
    return j

print(nbJours(5, 10, 2021, 8, 11, 2022))