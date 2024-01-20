tableau = [[5, 2, 7, 30], 
           [8, 12, 5, 4], 
           [3, 10, 13, 6]]

def max_2d(tableau):
    max_liste = []
    for sub in tableau:
        temp = sub.copy();sub.sort()
        max_liste.append(sub[-1])
    max_liste.sort()
    return max_liste[-1]

print(max_2d(tableau))