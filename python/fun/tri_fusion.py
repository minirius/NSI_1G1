def tri_fusion(liste:list):
    n = len(liste)
    if(n <= 1):
        return liste
    else:
        return fusion(tri_fusion(liste[0:n%2]), tri_fusion(liste[n//2:n]))

def fusion(A:list, B:list):
    if(len(A) == 0):
        return B
    if(len(B) == 0):
        return A
    if(A[1] <= B[1]):
        print(A[1] + fusion(A[2:-1], B))
        return A[1] + fusion(A[2:-1], B)
    else:
        print(B[1] + fusion(A, B[2:-1]))
        return B[1] + fusion(A, B[2:-1])

print(tri_fusion([3, 5, 1, 6, 7, 23, 78, 2, 6, 7]))