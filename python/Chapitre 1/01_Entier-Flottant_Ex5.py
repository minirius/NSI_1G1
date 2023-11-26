#input du temps en seconde de l'user dans la var userTime
userTime = input("Temps en seconde : ")

#Check si le userTime est un nombre valide (une chaine de digit) pour éviter les erreurs
if(userTime.isdigit()):
    #on converti sans créer d'erreur
    userTime = int(userTime)
else:
    #On print a l'utilisateur et on exit le programme
    print("La valeur entrée n'est pas valide")
    exit()

#Création de variable divisant le userTime en nombre entiers 
#Ex: 1min = 60sec soit tempMin = userTime / 60 
tempAnnées = userTime // 31536000
userTime -= tempAnnées*31536000
tempMois = userTime // (60*60*24*31)
userTime -= tempMois*(60*60*24*31)
tempDays = userTime // (60*60*24)
userTime -= tempDays*(60*60*24)
tempHour = userTime // 3600
userTime -= tempHour*3600
tempMin = userTime // 60
userTime -= tempMin*60

#print des variables en forme (ajout des unitées)
print(tempAnnées, "années ", tempMois, "mois ", tempDays, "j ", tempHour, "h", tempMin, "min ", userTime, "sec")