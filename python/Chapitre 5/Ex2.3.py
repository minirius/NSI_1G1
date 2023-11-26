n = input("nombre: ")
k = int(input("nombre de chiffre: "))
while(k > len(n)):
    n = input("n= ")
    k = int(input("k= "))

for i in range(1, len(n)//k+1):
    print(n[(len(n) - i*k):(len(n) - i*k)+k])