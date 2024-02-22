import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

SIZE=80
TABLEAU = [["" for j in range(8)] for i in range(8)]
THEME=0
LISTE_PIECE = {
    "tour" : [
        [f"caseX-{i+1};caseY" for i in range(8)],
        [f"caseX+{i+1};caseY" for i in range(8)],
        [f"caseX;caseY-{i+1}" for i in range(8)],
        [f"caseX;caseY+{i+1}" for i in range(8)],
    ],
    "fou" : [
        [f"caseX-{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX-{i+1};caseY+{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY+{i+1}" for i in range(8)],
    ],
    "cavalier" : [
        "caseX-2;caseY-1",
        "caseX-2;caseY+1",
        "caseX+2;caseY-1",
        "caseX+2;caseY+1",
        "caseX-1;caseY-2",
        "caseX+1;caseY-2",
        "caseX-1;caseY+2",
        "caseX+1;caseY+2",
    ],
    "reine" : [
        [f"caseX-{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX-{i+1};caseY+{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY+{i+1}" for i in range(8)],
        [f"caseX-{i+1};caseY" for i in range(8)],
        [f"caseX+{i+1};caseY" for i in range(8)],
        [f"caseX;caseY-{i+1}" for i in range(8)],
        [f"caseX;caseY+{i+1}" for i in range(8)],
    ],
    "roi" : [
        "caseX-1;caseY-1",
        "caseX-1;caseY+1",
        "caseX+1;caseY-1",
        "caseX+1;caseY+1",
        "caseX;caseY-1",
        "caseX;caseY+1",
        "caseX+1;caseY",
        "caseX-1;caseY",
    ],
}

def map(value , start1, end1, scale1, scale2):
    return int(((value*(scale2 - scale1))/(end1 - start1)) + scale1)

class Game(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.realSize = SIZE*8
        self.minsize(self.realSize, self.realSize)
        self.maxsize(self.realSize, self.realSize)
        self.title("Echec Tkinter")

        self.canvas = tk.Canvas(self, background='white', height=self.realSize, width=self.realSize, border=None)
        self.canvas.bind("<Button-1>", self.clickHandler)
        self.canvas.pack()
        self.tour = 0

        self.click_state = "unselected"
        self.setupTableau()
        self.drawScreen()
    
    def placeRed(self, x: int, y:int) -> None:
        self.canvas.create_rectangle((x*SIZE, y*SIZE), ((x+1)*SIZE, (y+1)*SIZE), outline="red", width=4)
        self.possibilities.append((x, y))
    
    def placeBlue(self, x: int, y:int) -> None:
        self.canvas.create_oval((x*SIZE+25, y*SIZE+25),((x+1)*SIZE-25, (y+1)*SIZE-25), fill="cadetblue2", width=0)
        self.possibilities.append((x, y))
    
    def placePoint(self, x: int, y:int) -> None:
        if(self.tour == 0):
            if("noir" in TABLEAU[y][x]):
                self.placeRed(x, y)
            elif TABLEAU[y][x] == "":
                self.placeBlue(x, y)
        elif(self.tour == 7):
            if("blanc" in TABLEAU[y][x]):
                self.placeRed(x, y)
            elif TABLEAU[y][x] == "":
                self.placeBlue(x, y)
            
    def debug(self, table):
        for i in table:
            for j in i:
                print(str(j).rjust(15), end="")
            print()
            
    def flip_tableau(self):
        global TABLEAU
        TEMP_TABLEAU = [["" for i in range(8)] for i in range(8)] 
        for x, e in enumerate(TABLEAU):
            for y, E in  enumerate(e):
                TEMP_TABLEAU[7-x][7-y] = E
        '''self.debug(TABLEAU)
        self.debug(TEMP_TABLEAU)'''
        TABLEAU = TEMP_TABLEAU.copy()
        self.tour = abs(self.tour - 7)
        self.drawScreen()
    
    def check_for_check(self):
        TEMP_TABLEAU = [e for e in TABLEAU if e!=""]
        for x, e in enumerate(TABLEAU):
            for y, E in enumerate(e):
                caseY, caseX = y, x
                if(self.tour == 0 and "noir" in TABLEAU[caseY][caseX]):
                    continue
                elif(self.tour == 7 and "blanc" in TABLEAU[caseY][caseX]):
                    continue
                elif(TABLEAU[caseY][caseX] == ""):
                    continue
                if("pion" in TABLEAU[caseY][caseX]):
                    try:
                        if("roi" in TABLEAU[caseY-1][caseX-1] and self.tour == 0):
                            return True
                        elif("roi" in TABLEAU[caseY-1][caseX+1] and self.tour == 0):
                            return True
                        elif("roi" in TABLEAU[caseY+1][caseX-1] and self.tour == 7):
                            return True
                        elif("roi" in TABLEAU[caseY+1][caseX+1] and self.tour == 7):
                            return True
                        else:
                            continue
                    except:
                        print("Out Range")
                        continue
                for move in LISTE_PIECE[TABLEAU[caseY][caseX].split("_")[0]]:
                        if(type(move) == str):
                            newCaseX = eval(move.split(";")[0])
                            newCaseY = eval(move.split(";")[1])
                            if(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                                continue
                            if("roi" in TABLEAU[newCaseY][newCaseX]):
                                return True
                        else:
                            for sub_move in move:
                                newCaseX = eval(sub_move.split(";")[0])
                                newCaseY = eval(sub_move.split(";")[1])
                                if(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                                    continue
                                if(TABLEAU[newCaseY][newCaseX] == ""):
                                    continue
                                elif("roi" in TABLEAU[newCaseY][newCaseX]):
                                    return True
                                break
        
    def clickHandler(self, event):
        self.drawScreen()
        x, y = event.x, event.y
        caseX = map(x, 0, self.realSize, 0, 8)
        caseY = map(y, 0, self.realSize, 0, 8)

        if(self.click_state == "unselected"):
            self.click_state = "selected"
            self.possibilities = []
            self.oldPos = (caseX, caseY)
            self.canvas.create_rectangle((caseX*SIZE+3, caseY*SIZE+3), ((caseX+1)*SIZE-3, (caseY+1)*SIZE-3), outline="chartreuse1", width=6)
            if(self.tour == 0 and "noir" in TABLEAU[caseY][caseX]):
                return                
            if(self.tour == 7 and "blanc" in TABLEAU[caseY][caseX]):
                return                
            if("pion" in TABLEAU[caseY][caseX]):
                newCaseX, newCaseY = caseX, caseY-1
                self.placePoint(newCaseX, newCaseY)

                if(caseY == 6 and TABLEAU[newCaseY][newCaseX] == ""):
                    newCaseX, newCaseY = caseX, caseY-2
                    self.placePoint(newCaseX, newCaseY)

                newCaseX, newCaseY = caseX-1, caseY-1
                if not(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                    if(self.tour == 0):
                        if("noir" in TABLEAU[newCaseY][newCaseX]):
                            self.placeRed(caseX, caseY)
                    else:
                        if("blanc" in TABLEAU[newCaseY][newCaseX]):
                            self.placeRed(caseX, caseY)
                
                newCaseX, newCaseY = caseX+1, caseY-1
                if not (0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                    if(self.tour == 0):
                        if("noir" in TABLEAU[newCaseY][newCaseX]):
                            self.placeRed(caseX, caseY)
                    else:
                        if("blanc" in TABLEAU[newCaseY][newCaseX]):
                            self.placeRed(caseX, caseY)

            elif(TABLEAU[caseY][caseX] and TABLEAU[caseY][caseX].split("_")[0] in LISTE_PIECE):
                for move in LISTE_PIECE[TABLEAU[caseY][caseX].split("_")[0]]:
                    if(type(move) == str):
                        newCaseX = eval(move.split(";")[0])
                        newCaseY = eval(move.split(";")[1])
                        if(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                            continue
                        self.placePoint(newCaseX, newCaseY)
                    else:
                        for sub_move in move:
                            newCaseX = eval(sub_move.split(";")[0])
                            newCaseY = eval(sub_move.split(";")[1])
                            if(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                                continue
                            if(TABLEAU[newCaseY][newCaseX] == ""):
                                self.placeBlue(newCaseX, newCaseY)
                                continue
                            if(self.tour == 0):
                                if("noir" in TABLEAU[newCaseY][newCaseX]):
                                    self.placeRed(newCaseX, newCaseY)
                            elif(self.tour == 7):
                                if("blanc" in TABLEAU[newCaseY][newCaseX]):
                                    self.placeRed(newCaseX, newCaseY)
                            break

        else:
            if((caseX, caseY) in self.possibilities):
                print("Moved !")
                TABLEAU[caseY][caseX] = TABLEAU[self.oldPos[1]][self.oldPos[0]]
                TABLEAU[self.oldPos[1]][self.oldPos[0]] = ""
                self.drawScreen()
                print(self.check_for_check())
                self.after(500, self.flip_tableau)

            self.click_state = "unselected"
            self.possibilities = []
            self.oldPos = (0, 0)
    
    def drawScreen(self):
        self.canvas.delete("all")
        self.images = []
        for i in range(64):
            X = i%8
            Y = i//8
            match THEME:
                case 1:
                    color = "coral4" if (X+Y)%2 else "aliceblue"
                case 2:
                    color = "burlywood4" if (X+Y)%2 else "burlywood1"
                case 3:
                    color = "lightcyan4" if (X+Y)%2 else "linen"
                case 4:
                    color = "darkgoldenrod2" if (X+Y)%2 else "gray98"
                case 5:
                    color = "forestgreen" if (X+Y)%2 else "darkolivegreen2"

            self.canvas.create_rectangle(((X)*SIZE, (Y)*SIZE), ((X+1)*SIZE, (Y+1)*SIZE), fill=color)
            if(TABLEAU[i//8][i%8] != ""):
                self.images.append(tk.PhotoImage(file=f"python/jeu_echec/{TABLEAU[i//8][i%8]}.png"))
                self.canvas.create_image((X)*SIZE+10, (Y)*SIZE+10, image = self.images[-1], anchor = tk.NW)

    def setupTableau(self):
        TABLEAU[7] = ["tour_blanc", "cavalier_blanc", "fou_blanc", "reine_blanc", "roi_blanc", "fou_blanc", "cavalier_blanc", "tour_blanc"]
        TABLEAU[6] = ["pion_blanc" for i in range(8)]
        TABLEAU[0] = ["tour_noir", "cavalier_noir", "fou_noir", "reine_noir", "roi_noir", "fou_noir", "cavalier_noir", "tour_noir"]
        TABLEAU[1] = ["pion_noir" for i in range(8)]
        print(TABLEAU)

if __name__ == "__main__":
    #IP_ADRR = simpledialog.askstring("IP Adresse", "Veuillez entrer l'IP de votre adversaire")
    ROOM = messagebox.askyesnocancel("Game", "Yes : Créer une partie\nNo: Rejoindre une partie")
    if(ROOM == None):
        quit()
    elif(ROOM):
        ...
    else:
        ...

    THEME = int(simpledialog.askstring("Thème", "Veuillez un de thème suivant (1)-5)\n\t1: Safran\n\t2: Bois\n\t3: Bleuté\n\t4:Jaune\n\t5: Emmeraude"))
    if THEME > 6 or THEME < 1:
        THEME = 1
    app = Game()
    app.mainloop()