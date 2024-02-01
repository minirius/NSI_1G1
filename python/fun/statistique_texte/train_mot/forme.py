import os

mode = input(": ")

if(mode == "1"):
    os.chdir(os.getcwd()+'/python/fun/statistique_texte/train_mot')
    texte = open("balzac.txt", mode='r', encoding='UTF-8')
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
    FinalText = FinalText.replace("- ", "")
    FinalText = FinalText.replace("– ", "")
    FinalText = FinalText.replace("― ", "")
    FinalText = FinalText.replace(",", "")
    FinalText = FinalText.replace(".", "")
    FinalText = FinalText.replace(";", "")
    FinalText = FinalText.replace(":", "")
    FinalText = FinalText.replace("!", "")
    FinalText = FinalText.replace("?", "")
    FinalText = FinalText.replace("…", "")
    banned_char = ["- ", "– ", "― ", ",", ".", ";", ":", "!", "?", "…", "\u202f"]
    for i in banned_char:
        FinalText = FinalText.replace(i, "")
    for i in range(10):
        FinalText = FinalText.replace("  ", " ")
    file.write(FinalText) 
    file.close() 