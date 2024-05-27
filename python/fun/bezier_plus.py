from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import math
import os

WIDTH = 800
HEIGHT = 800
LISTE_NOTE = []
NIVEAU = 6

def bernstein(v, n, x):
    binomial = (math.factorial(n))/(math.factorial(v)*math.factorial(n-v))
    return binomial*(x**v)*((1-x)**(n-v))

def bezier_x(liste, n, x):
    total = 0
    for v in range(0, n):
        total += bernstein(v, n-1, x)*liste[v][0]
    return total

def bezier_y(liste, n, x):
    total = 0
    for v in range(0, n):
        total += bernstein(v, n-1, x)*liste[v][1]
    return total

class App:
    def __init__(self, master):
        self.POINTS = []
        self.COLOR = "red"
        self.ROUNDED = True
        self.THICKNESS = 2
        self.curve = None

        self.canvas = Canvas(master, width=800, height=800, bg="white")
        self.canvas.bind("<Button-1>", self.place_point)
        self.canvas.pack()

        self.menu = Menu(master)
        master.config(menu=self.menu)

        self.fileMenu = Menu(self.menu, tearoff=False)
        self.fileMenu.add_command(label="Enregister", command=self.save)
        self.fileMenu.add_command(label="Effacer Tout", command=self.delete)
        self.fileMenu.add_command(label="Ouvrir", command=self.save)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quitter", command=quit)
        self.menu.add_cascade(label="Fichier", menu=self.fileMenu)

        """
        self.editMenu = Menu(self.menu, tearoff=False)
        self.editMenu.add_command(label="Ajouter")
        self.editMenu.add_command(label="Supprimer")
        self.menu.add_cascade(label="Outils", menu=self.editMenu)"""

        self.settingsMenu = Menu(self.menu, tearoff=False)
        self.settingsMenu.add_command(label="Points", command=self.modifier_points)
        self.settingsMenu.add_command(label="Modifier", command=self.settings)
        self.menu.add_cascade(label="Paramètre", menu=self.settingsMenu)

    def modifier_points(self):
        ...
        
    def delete(self):
        self.POINTS = []
        self.canvas.delete('all')

    def settings(self):
        ...

    def save(self):
        f = filedialog.asksaveasfile(defaultextension=".svg", filetypes=[("SVG Images", '*.svg')])
        file = open(f.name, "w+")
        try:
            N = len(self.POINTS)
            file.write("""<?xml version="1.0" encoding="utf-8" standalone="no"?>
<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" version="1.1">
    <path d=" """)

            minX = 800
            minY = 800
            X = []
            Y = []
            for i in np.arange(0, 1, .01):
                x = round(bezier_x(self.POINTS, N, i), 4)
                y = round(bezier_y(self.POINTS, N, i), 4)
                if(minX > x) : minX = x
                if(minY > y) : minY = y
                X.append(x)
                Y.append(y)

            for i in range(0, 100):
                if(i == 0):
                    file.write("M "+str(X[i]-minX+5)+" "+str(Y[i]-minY+5)+"\n")
                else:
                    file.write("L "+str(X[i]-minX+5)+" "+str(Y[i]-minY+5)+"\n")

            file.write(""" " style="fill: none; stroke: """+self.COLOR+"""; stroke-width: """+str(self.THICKNESS)+"""; stroke-linecap: round"/>\n</svg>""")
        finally:
            file.close()

        os.startfile(f.name)

    def draw_curve(self):
        N = len(self.POINTS)
        X = []
        Y = []
        for i in np.arange(0, 1, .001):
            X.append(bezier_x(self.POINTS, N, i))
            Y.append(bezier_y(self.POINTS, N, i))
        liste = list(zip(X, Y))
    
        if(self.curve): self.canvas.delete(self.curve)
        self.curve = self.canvas.create_line(liste, width=self.THICKNESS, fill=self.COLOR, smooth=0)

    def place_point(self, event):
        print(event)
        WIDTH = 8
        x1, y1 = (event.x - (WIDTH/2)), (event.y - (WIDTH/2))
        x2, y2 = (event.x + (WIDTH/2)), (event.y + (WIDTH/2))
        self.canvas.create_oval(x1, y1, x2, y2, fill="black")

        self.POINTS.append((event.x, event.y))
        self.draw_curve()

def main():
    root = Tk()
    root.minsize(WIDTH, HEIGHT)
    root.maxsize(WIDTH, HEIGHT)
    root.title("Courbe de bézier")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()