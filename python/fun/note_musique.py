from tkinter import *
import random

WIDTH = 800
HEIGHT = 500
LISTE_NOTE = []
NIVEAU = 6

def changeNote():
    global NIVEAU, LISTE_NOTE
    LISTE_NOTE = []
    for i in range((WIDTH - 40)//30):
        if(i == 0): LISTE_NOTE.append(random.randint(0, 14))
        else:
            limUp = LISTE_NOTE[i-1] + NIVEAU
            if(limUp > 14): limUp = 14
            limDown = LISTE_NOTE[i-1] - NIVEAU
            if(limDown < 0): limDown = 0

            LISTE_NOTE.append(random.randint(limDown, limUp))

class App:
    def __init__(self, master):
        self.canvas = Canvas(master, width=WIDTH, height=HEIGHT-80, bg='white')
        self.canvas.pack(side="top")

        self.button = Button(master, text="aléatoire !", command=self.update_note)
        self.button.pack(side="bottom", pady=20)

    def update(self):
        global LISTE_NOTE
        self.canvas.delete('all')
        for i in range(5):
            self.canvas.create_line((0, 150+i*20), (WIDTH, 150+i*20), fill="black", width=3)

        for i in range(0, (WIDTH - 40)//30):
            note = LISTE_NOTE[i]
            self.canvas.create_oval((20+i*30, 110+note*10), (40+i*30, 130+note*10), fill="black", outline="black" ,width=1)
            if(0<=note and note<2):
                self.canvas.create_line((12+i*30, 130), (48+i*30, 130), fill="black", width=3)
            if (12<note and note<=14):
                self.canvas.create_line((12+i*30, 250), (48+i*30, 250), fill="black", width=3)
    def update_note(self):
        changeNote()
        self.update()

def main():
    global LISTE_NOTE, NIVEAU
    NIVEAU = int(input("Niveau : "))
    changeNote()

    root = Tk()
    root.minsize(WIDTH, HEIGHT)
    root.maxsize(WIDTH, HEIGHT)
    root.title("Lecture de Note aleatoire")
    app = App(root)
    app.update()
    root.mainloop()

if __name__ == "__main__":
    main()