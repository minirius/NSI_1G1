def tableau_aleatoire(n:int):
    import random


    assert type(n) == int
    assert n > 1

    return [random.randint(1, n-1) for i in range(n)]

def doublons(tab:list):
    assert type(tab) == list
    assert len(tab) > 1

    return_list = {}
    for e in tab:
        if(tab.count(e) > 1): return_list[e] = tab.count(e)
    return return_list

def verifie_doublons(tab:list, r:int):
    assert type(tab) == list
    assert len(tab) > 1

    return tab.count(r) > 1


def test(tab):
    import random

    doubles = doublons(tab)
    if(doubles == None): return True
    for db in doubles.keys():
        if(not verifie_doublons(tab, db)):
            return False

    return True

if(__name__ == "__main__"):
    '''myTab = tableau_aleatoire(10)
    print(myTab)
    print(doublons(myTab))
    print(verifie_doublons(myTab, 5))'''

    for n in range(2, 22):
        for _ in range(10):
            tab = tableau_aleatoire(n)
            assert test(tab)

    print("OKAY")