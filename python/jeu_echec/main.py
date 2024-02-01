import time
import tkinter as tk

SIZE=80
TABLEAU = [["" for j in range(8)] for i in range(8)]
LISTE_PIECE = {
    "pion_blanc" : [
        "caseX;caseY-1",
    ],
    "tour_blanc" : [
        [f"caseX-{i+1};caseY" for i in range(8)],
        [f"caseX+{i+1};caseY" for i in range(8)],
        [f"caseX;caseY-{i+1}" for i in range(8)],
        [f"caseX;caseY+{i+1}" for i in range(8)],
    ],
    "fou_blanc" : [
        [f"caseX-{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX-{i+1};caseY+{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY+{i+1}" for i in range(8)],
    ],
    "cavalier_blanc" : [
        "caseX-2;caseY-1",
        "caseX-2;caseY+1",
        "caseX+2;caseY-1",
        "caseX+2;caseY+1",
        "caseX-1;caseY-2",
        "caseX+1;caseY-2",
        "caseX-1;caseY+2",
        "caseX+1;caseY+2",
    ],
    "reine_blanc" : [
        [f"caseX-{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX-{i+1};caseY+{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY-{i+1}" for i in range(8)],
        [f"caseX+{i+1};caseY+{i+1}" for i in range(8)],
        [f"caseX-{i+1};caseY" for i in range(8)],
        [f"caseX+{i+1};caseY" for i in range(8)],
        [f"caseX;caseY-{i+1}" for i in range(8)],
        [f"caseX;caseY+{i+1}" for i in range(8)],
    ],
    "roi_blanc" : [
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
    #
    # value         scaleValue
    # val2 - val1   scale2 - scale1
    #
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
            if(TABLEAU[caseY][caseX]=="pion_blanc"):
                newCaseX, newCaseY = caseX, caseY-1
                if("noir" in TABLEAU[newCaseY][newCaseX]):
                    self.canvas.create_rectangle((newCaseX*SIZE, newCaseY*SIZE), ((newCaseX+1)*SIZE, (newCaseY+1)*SIZE), outline="red", width=4)
                    self.possibilities.append((newCaseX, newCaseY))
                elif TABLEAU[newCaseY][newCaseX] == "":
                    self.canvas.create_oval((newCaseX*SIZE+25, newCaseY*SIZE+25),((newCaseX+1)*SIZE-25, (newCaseY+1)*SIZE-25), fill="cadetblue2", width=0)
                    self.possibilities.append((newCaseX, newCaseY))

                if(caseY == 6 and TABLEAU[newCaseY][newCaseX] == ""):
                    newCaseX, newCaseY = caseX, caseY-2
                    if("noir" in TABLEAU[newCaseY][newCaseX]):
                        self.canvas.create_rectangle((newCaseX*SIZE, newCaseY*SIZE), ((newCaseX+1)*SIZE, (newCaseY+1)*SIZE), outline="red", width=4)
                        self.possibilities.append((newCaseX, newCaseY))
                    elif TABLEAU[newCaseY][newCaseX] == "":
                        self.canvas.create_oval((newCaseX*SIZE+25, newCaseY*SIZE+25),((newCaseX+1)*SIZE-25, (newCaseY+1)*SIZE-25), fill="cadetblue2", width=0)
                        self.possibilities.append((newCaseX, newCaseY))

                newCaseX, newCaseY = caseX-1, caseY-1
                if not(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                    if("noir" in TABLEAU[newCaseY][newCaseX]):
                        self.canvas.create_rectangle((newCaseX*SIZE, newCaseY*SIZE), ((newCaseX+1)*SIZE, (newCaseY+1)*SIZE), outline="red", width=4)
                        self.possibilities.append((newCaseX, newCaseY))
                
                newCaseX, newCaseY = caseX+1, caseY-1
                if not (0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                    if("noir" in TABLEAU[newCaseY][newCaseX]):
                        self.canvas.create_rectangle((newCaseX*SIZE, newCaseY*SIZE), ((newCaseX+1)*SIZE, (newCaseY+1)*SIZE), outline="red", width=4)
                        self.possibilities.append((newCaseX, newCaseY))
            elif(TABLEAU[caseY][caseX] and TABLEAU[caseY][caseX] in LISTE_PIECE):
                for move in LISTE_PIECE[TABLEAU[caseY][caseX]]:
                    if(type(move) == str):
                        newCaseX = eval(move.split(";")[0])
                        newCaseY = eval(move.split(";")[1])
                        if(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                            continue
                        if(TABLEAU[newCaseY][newCaseX] == ""):
                            self.canvas.create_oval((newCaseX*SIZE+25, newCaseY*SIZE+25),((newCaseX+1)*SIZE-25, (newCaseY+1)*SIZE-25), fill="cadetblue2", width=0)
                            self.possibilities.append((newCaseX, newCaseY))
                        elif("noir" in TABLEAU[newCaseY][newCaseX]):
                            self.canvas.create_rectangle((newCaseX*SIZE, newCaseY*SIZE), ((newCaseX+1)*SIZE, (newCaseY+1)*SIZE), outline="red", width=4)
                            self.possibilities.append((newCaseX, newCaseY))
                    else:
                        for sub_move in move:
                            newCaseX = eval(sub_move.split(";")[0])
                            newCaseY = eval(sub_move.split(";")[1])
                            if(0 > newCaseX or newCaseX > 7 or 0 > newCaseY or newCaseY > 7):
                                continue
                            if(TABLEAU[newCaseY][newCaseX] == ""):
                                self.canvas.create_oval((newCaseX*SIZE+25, newCaseY*SIZE+25),((newCaseX+1)*SIZE-25, (newCaseY+1)*SIZE-25), fill="cadetblue2", width=0)
                                self.possibilities.append((newCaseX, newCaseY))
                            elif("noir" in TABLEAU[newCaseY][newCaseX]):
                                self.canvas.create_rectangle((newCaseX*SIZE, newCaseY*SIZE), ((newCaseX+1)*SIZE, (newCaseY+1)*SIZE), outline="red", width=4)
                                self.possibilities.append((newCaseX, newCaseY))
                                break
                            else:
                                break

        else:
            if((caseX, caseY) in self.possibilities):
                print("Moved !")
                TABLEAU[caseY][caseX] = TABLEAU[self.oldPos[1]][self.oldPos[0]]
                TABLEAU[self.oldPos[1]][self.oldPos[0]] = ""
                #self.tour = abs(self.tour - 7)
                self.drawScreen()

            self.click_state = "unselected"
            self.possibilities = []
            self.oldPos = (0, 0)
    
    def drawScreen(self):
        self.canvas.delete("all")
        self.images = []
        for i in range(64):
            X = abs(self.tour - i%8)
            Y = abs(self.tour - i//8)
            print(self.tour, X, Y, i%8, i//8)
            color = "coral4" if (X+Y)%2 else "aliceblue"
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
    app = Game()
    app.mainloop()