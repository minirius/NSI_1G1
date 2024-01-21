import os

mode = input(": ")

if(mode == "1"):
    os.chdir(os.getcwd()+'/python/fun/statistique_texte/train_mot')
    texte = open("master_balzac.txt", mode='r', encoding='UTF-8')
    FinalText = []
    for e in texte.readlines():
        FinalText.append(e.strip())
    texte.close()
    file = open("balzac.txt", "w", encoding='UTF-8') 
    file.write(" ".join(FinalText)) 
    file.close() 
elif mode == "2":
    os.chdir(os.getcwd()+'/python/fun/statistique_texte/train_mot')
    texte = open("balzac.txt", mode='r', encoding='UTF-8')
    FinalText = texte.read()
    texte.close()
    file = open("balzac.txt", "w", encoding='UTF-8') 
    file.write(FinalText.replace("  ", " ").replace("   ", " ").replace("    ", " ").replace("     ", " ")) 
    file.close() 