print("Convertions : ")
print(">> 1: Celsius => Fehrenheit")
print(">> 2: Fehrenheit => Celsius")
choix = input(">>> ")

if(choix == "1"):
    nbr = float(input("Température (en °C): "))
    print(nbr , "°C =>", round((nbr*1.8)+32, 2), "°F")
elif(choix == "2"):
    nbr = float(input("Température (en °F): "))
    print(nbr , "°F =>", round((nbr-32)/1.8, 2), "°C")
else:
    print("Veuillez un nombre valide entre 1 et 2")