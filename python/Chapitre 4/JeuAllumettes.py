import tkinter as tk
import random

root = tk.Tk()
root.title("Jeux d'alumettes")
root.geometry("400x640")
root.resizable(False, False)

text = tk.StringVar()
text.set('Jouez')

jeux_joueur = 0
nbr_allumettes = 21
colors = ["blue", "yellow", "green", "red", "black"]
proba = 30
didPlayerWin = False

def tksleep(self, time:float) -> None:
    self.after(int(time*1000), self.quit)
    self.mainloop()
tk.Misc.tksleep = tksleep

canva = tk.Canvas(root, height=510, width=400, bg="white")
canva.place(x=0, y=0)

def message(*args):
    final_message = ""
    for i in args:
        final_message += str(i)+" "
    final_message = final_message.strip()
    text.set(final_message)

def AI(a):
    playhard = random.randint(0, 100)
    if(playhard <= proba):
        nbrRestant = nbr_allumettes % 4
        if nbrRestant == 0:
            b = 3
        elif nbrRestant == 3:
            b = 2
        elif nbrRestant == 2:
            b = 1
        elif nbrRestant == 1:
            b = 2
    else:
        nbrRestant = nbr_allumettes % 4
        if nbrRestant == 0:
            b = random.randint(2, 3)
        elif nbrRestant == 3:
            b = random.randint(1, 2)
        elif nbrRestant == 2:
            b = random.randint(1, 3)
        elif nbrRestant == 1:
            b = random.randint(1, 3)
    return b

def afficher():
    global canva
    canva.delete("all") 
    for i in range(nbr_allumettes):
        index = i%len(colors)
        canva.create_rectangle(50+15*i, 200, 15*i + 52, 400, fill=colors[index])

def rejouer(replayButton):
    global didPlayerWin, canva, proba
    if(didPlayerWin):
        proba *= 1.5
    else:
        proba /= 1.5
    proba = int(proba)
    canva.delete("all")
    replayButton["state"] = "disable"
    afficher()

replayButton = tk.Button(root, command=lambda: rejouer(replayButton), text="Rejouer !")
replayButton.place(x=20, y=595, width=360, height=30)
replayButton["state"] = "disabled"

def jouer(jeux_joueur):
    global nbr_allumettes, didPlayerWin, canva, replayButton
    nbr_allumettes -= jeux_joueur
    afficher()
    if(nbr_allumettes <= 0):
        message("Vous avez perdu !")
        replayButton["state"] = "normal"
    else:
        message("...")
        root.tksleep(1)
        jeux_ai = AI(jeux_joueur)
        nbr_allumettes -= jeux_ai
        message("J'en ai pris", jeux_ai)
        if(nbr_allumettes <= 0):
            didPlayerWin = True
            replayButton["state"] = "normal"
            message("Vous avez gagné !")
    afficher()


tk.Label(root, textvariable=text, justify="center").place(x=0, y=520, width=400, height=30, )
tk.Button(root, command=lambda: jouer(1), text="Pendre 1").place(x=20, y=560, width=110, height=25)
tk.Button(root, command=lambda: jouer(2), text="Pendre 2").place(x=150, y=560, width=110, height=25)
tk.Button(root, command=lambda: jouer(3), text="Pendre 3").place(x=270, y=560, width=110, height=25)

afficher()
root.mainloop()