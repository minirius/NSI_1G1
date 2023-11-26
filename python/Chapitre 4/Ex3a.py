a  = abs(int(input("Entrer un nombre naturel :")))
i = 0
while a != 0:
    a //= 10
    i += 1
print(i)