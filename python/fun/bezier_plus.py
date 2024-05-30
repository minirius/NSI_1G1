from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import xml.etree.ElementTree as ET
import numpy as np
import math
import os

WIDTH = 600
HEIGHT = 600

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
        self.hover_point = None
        self.hover_coords = None
        self.start_moving = False
        self.master = master
        self.open_file_path = ""
        self.modified = False

        self.canvas = Canvas(master, width=800, height=800, bg="white")
        self.canvas.bind("<ButtonPress-1>", self.place_point)
        self.canvas.bind("<ButtonRelease-1>", self.move_point)
        self.canvas.bind("<Button-2>", self.delete_point)
        self.canvas.pack()

        self.menu = Menu(master)
        master.config(menu=self.menu)

        self.fileMenu = Menu(self.menu, tearoff=False)
        self.fileMenu.add_command(label="Enregister", command=self.save)
        self.fileMenu.add_command(label="Effacer Tout", command=self.delete)
        self.fileMenu.add_command(label="Ouvrir", command=self.open_file)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Quitter", command=self.closing)
        self.menu.add_cascade(label="Fichier", menu=self.fileMenu)

        self.settingsMenu = Menu(self.menu, tearoff=False)
        self.settingsMenu.add_command(label="Points", command=self.modifier_points)
        self.settingsMenu.add_command(label="Modifier", command=self.settings)
        self.menu.add_cascade(label="Paramètre", menu=self.settingsMenu)

        self.aboutMenu = Menu(self.menu, tearoff=False)
        self.aboutMenu.add_command(label="En savoir plus...", command=self.about)
        self.menu.add_cascade(label="A propos", menu=self.aboutMenu)

    def about(self):
        top = Toplevel()
        top.title("A propos")
        top.geometry("400x350")

        Label(top, text="Bézier+", font='tkDefaeultFont 30').grid(pady=10)
        Label(top, text="Un logiciel de graphisme SVG avec les courbes de bézier", font='tkDefaeultFont 12').grid()

        Label(top, text="", font='tkDefaeultFont 12').grid(pady=20)
        
        Label(top, text="Clique Gauche : Placer un point", font='tkDefaeultFont 12').grid()
        Label(top, text="Clique Droit : Supprimer un point", font='tkDefaeultFont 12').grid()
        Label(top, text="Drag & Drop : Déplacer un point", font='tkDefaeultFont 12').grid()

        Label(top, text="", font='tkDefaeultFont 12').grid(pady=20)

        Label(top, text="By Minirius", font='tkDefaeultFont 12').grid(pady=20)

        top.columnconfigure(0, weight=100)

        top.mainloop()

    def modifier_points(self):
        top = Toplevel()
        top.title("Points")
        top.geometry("300x400")

        listStringVarX = []
        listStringVarY = []
        listWidgetX = []
        listWidgetY = []
        listWidgetName = []

        def save_points(event):
            if(self.open_file_path != ""):
                self.master.title("(*) Bezier+ | "+os.path.basename(self.open_file_path))
            else: 
                self.master.title("(*) Bezier+ | Nouveau Fichier")
            self.modified = True
            for i in range(len(self.POINTS)):
                x = int(listStringVarX[i].get())
                y = int(listStringVarY[i].get())
                self.POINTS[i] = (x, y)
                top.destroy()
                self.refresh()

        Label(top, text="Point").grid(row=0, column=0, sticky=EW)
        Label(top, text="X").grid(row=0, column=1, sticky=EW)
        Label(top, text="Y").grid(row=0, column=2, sticky=EW)

        for i, p in enumerate(self.POINTS):
            listWidgetName.append(Label(top, text="P"+str(i)))
            listWidgetName[i].grid(row=i+1, column=0, sticky=EW)

            listStringVarX.append(StringVar(top, p[0]))
            listStringVarY.append(StringVar(top, p[1]))

            listWidgetX.append(Entry(top, width=5, textvariable=listStringVarX[i]))
            listWidgetX[i].grid(row=i+1, column=1, sticky=EW)
            listWidgetX[i].bind("<Return>", save_points)

            listWidgetY.append(Entry(top, width=5, textvariable=listStringVarY[i]))
            listWidgetY[i].grid(row=i+1, column=2, sticky=EW)
            listWidgetY[i].bind("<Return>", save_points)

            top.rowconfigure(i+1, weight=20)

        top.rowconfigure(0, weight=2)
        top.columnconfigure(0, weight=50)
        top.columnconfigure(1, weight=150)
        top.columnconfigure(2, weight=150)

        top.mainloop()
        
    def delete(self):
        self.POINTS = []
        self.canvas.delete('all')
        if(self.open_file_path != ""):
                self.master.title("(*) Bezier+ | "+os.path.basename(self.open_file_path))
        else: 
            self.master.title("(*) Bezier+ | Nouveau Fichier")
        self.modified = True
    
    def refresh(self):
        self.canvas.delete('all')
        self.draw_curve()
        self.draw_points()

    def settings(self):
        top = Toplevel()
        top.geometry("400x100")
        top.title("Paramètre")

        def update(event):
            self.THICKNESS = float(textVariableThickness.get())
            self.COLOR = textVariableColor.get()
            if(self.open_file_path != ""):
                self.master.title("(*) Bezier+ | "+os.path.basename(self.open_file_path))
            else: 
                self.master.title("(*) Bezier+ | Nouveau Fichier")
            self.modified = True
            self.refresh()
            top.destroy()

        textVariableThickness = StringVar(top, self.THICKNESS)
        labelThickness = Label(top, text="Epaisseur (en px)")
        labelThickness.grid(row=0, column=0)
        entryThickness = Entry(top, textvariable=textVariableThickness)
        entryThickness.grid(row=0, column=1)
        entryThickness.bind("<Return>", update)

        textVariableColor = StringVar(top, self.COLOR)
        labelColor = Label(top, text="Couleur (anglais)")
        labelColor.grid(row=1, column=0)
        entryColor = Entry(top, textvariable=textVariableColor)
        entryColor.grid(row=1, column=1)
        entryColor.bind("<Return>", update)

        top.rowconfigure(0, weight=10)
        top.rowconfigure(1, weight=10)
        top.columnconfigure(0, weight=50)
        top.columnconfigure(1, weight=50)

        top.mainloop()

    def draw_points(self):
        for i, p in enumerate(self.POINTS):
            x, y = p
            x1, y1 = (x - (8/2)), (y - (8/2))
            x2, y2 = (x + (8/2)), (y + (8/2))
            self.canvas.create_oval(x1, y1, x2, y2, fill="black")
            self.canvas.create_text((x+15, y+15), text="P"+str(i), fill="black", font='tkDefaeultFont 12')


    def hover(self, event):
        if(event.x > 600 or event.x < 0) or (event.y > 600 or event.y < 0): return

        self.isHovering = False
        for p in self.POINTS:
            if (abs(p[0] - event.x) < 12 and abs(p[1] - event.y) < 12):
                x1, y1 = (p[0] - (12/2)), (p[1] - (12/2))
                x2, y2 = (p[0] + (12/2)), (p[1] + (12/2))
                self.hover_point = self.canvas.create_oval(x1, y1, x2, y2, fill=None, outline="lightblue", width=3)
                self.canvas.create_text((300, 580), text="X="+str(p[0])+" ; Y="+str(p[1]))
                self.isHovering = True
                self.hover_coords = p
                break

        if(self.start_moving):
            if(not self.modified):
                if(self.open_file_path != ""):
                    self.master.title("(*) Bezier+ | "+os.path.basename(self.open_file_path))
                else: 
                    self.master.title("(*) Bezier+ | Nouveau Fichier")
                self.modified = True

            index = self.POINTS.index(self.hover_coords)
            self.POINTS[index] = (event.x, event.y)
            self.hover_coords = (event.x, event.y)
            self.refresh()
            self.canvas.create_text((300, 580), text="X="+str(event.x)+" ; Y="+str(event.y))

        if(not self.isHovering):
            self.refresh()

    def open_file(self):
        f = filedialog.askopenfilename(defaultextension=".svg", filetypes=[("SVG Images", '.svg')])
        self.master.title("Bezier+ | "+os.path.basename(f))
        self.open_file_path = f
        tree = ET.parse(f)
        root = tree.getroot()
        self.delete()

        for i, e in enumerate(root[1][0].iter()):
            if(e.attrib != {}):
                x, y = int(e.attrib["x"]), int(e.attrib["y"])
                self.POINTS.append((x, y))
                x1, y1 = (x - (8/2)), (y - (8/2))
                x2, y2 = (x + (8/2)), (y + (8/2))
                self.canvas.create_oval(x1, y1, x2, y2, fill="black")
                self.canvas.create_text((x+15, y+15), text="P"+str(i-1), fill="black", font='tkDefaeultFont 12')
        
        self.COLOR = root[1][1].attrib["value"]
        self.THICKNESS = float(root[1][2].attrib["value"])

        self.modified = False
        self.draw_curve()

    def save(self, event=None):
        if(self.open_file_path != ""):
            file = open(self.open_file_path, "w+")
            self.master.title("Bezier+ | "+os.path.basename(self.open_file_path))
            print("FileOk")
        else: 
            f = filedialog.asksaveasfile(defaultextension=".svg", filetypes=[("SVG Images", '.svg')])
            self.open_file_path = f.name
            self.master.title("Bezier+ | "+os.path.basename(f.name))
            if(f.name is None): return
            file = open(f.name, "w+")

        self.modified = False

        try:
            N = len(self.POINTS)
            file.write("""<?xml version="1.0" encoding="utf-8" standalone="no"?>\n<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" version="1.1">\n\t<path d=" """)

            minX = 601
            minY = 601
            X = []
            Y = []
            for i in np.arange(0, 1, .002):
                x = round(bezier_x(self.POINTS, N, i), 4)
                y = round(bezier_y(self.POINTS, N, i), 4)
                if(minX > x) : minX = x
                if(minY > y) : minY = y
                X.append(x)
                Y.append(y)

            for i in range(0, 500):
                if(i == 0):
                    file.write("M "+str(X[i]-minX+5)+" "+str(Y[i]-minY+5)+"\n")
                else:
                    file.write("L "+str(X[i]-minX+5)+" "+str(Y[i]-minY+5)+"\n")

            file.write(""" " style="fill: none; stroke: """+self.COLOR+"""; stroke-width: """+str(self.THICKNESS)+"""; stroke-linecap: round"/>\n\t<BezierPlusInfo>\n\t\t<PointsList>\n""")

            print(self.POINTS)
            for p in self.POINTS:
                file.write("""\t\t\t<p x='"""+str(p[0])+"""' y='"""+str(p[1])+"""'/>\n""")
            
            file.write("""\t\t</PointsList>\n\t\t<Color value='"""+str(self.COLOR)+"""' />\n\t\t<Thickness value='"""+str(self.THICKNESS)+"""' />""")
            file.write("""</BezierPlusInfo>\n</svg>""")

        finally:
            file.close()

            #os.system("open "+f.name)

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
        if(self.isHovering): self.start_moving = True; return
            
        else:
            if(self.open_file_path != ""):
                self.master.title("(*) Bezier+ | "+os.path.basename(self.open_file_path))
            else: 
                self.master.title("(*) Bezier+ | Nouveau Fichier")
            self.modified = True
            x1, y1 = (event.x - (8/2)), (event.y - (8/2))
            x2, y2 = (event.x + (8/2)), (event.y + (8/2))
            self.canvas.create_oval(x1, y1, x2, y2, fill="black")
            self.canvas.create_text((event.x+15, event.y+15), text="P"+str(len(self.POINTS)), fill="black", font='tkDefaeultFont 12')

            self.POINTS.append((event.x, event.y))
            self.draw_curve()

    def move_point(self, event):
        if not self.start_moving: return

        self.start_moving = False
        self.isHovering = True

        self.refresh()
    
    def delete_point(self, event):
        if(len(self.POINTS) == 0): return
        if(self.isHovering):
            self.POINTS.remove(self.hover_coords)
            self.refresh()

            if(self.open_file_path != ""):
                self.master.title("(*) Bezier+ | "+os.path.basename(self.open_file_path))
            else: 
                self.master.title("(*) Bezier+ | Nouveau Fichier")
            self.modified = True
        
    def closing(self):
        if(self.modified):
            if(messagebox.askokcancel(title="Modification non Sauvegardées", message="Voulez-vous vraiment quitter Bezier+ ?")):
                self.master.destroy()
        else:
            self.master.destroy()


def main():
    root = Tk()
    root.minsize(WIDTH, HEIGHT)
    root.maxsize(WIDTH, HEIGHT)
    root.title("Bezier+ | Nouveau Fichier")
    app = App(root)
    root.bind('<Motion>', app.hover)
    root.bind('<Control-s>', app.save)
    root.bind('<Command-s>', app.save)
    root.protocol("WM_DELETE_WINDOW", app.closing)
    root.mainloop()

if __name__ == "__main__":
    main()