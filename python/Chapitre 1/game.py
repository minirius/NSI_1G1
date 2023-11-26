import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("My Game")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

posX, posY = 0, 0
player = canvas.create_rectangle

def update():
    global player
    canvas.delete("all")
    player(posX, posY, posX+10, posY+10, fill="black")


def up():
    global posX, posY
    posY += 1
    update()

def down():
    global posX, posY
    posY -= 1
    update()

def right():
    global posX, posY
    posX += 1
    update()

def left():
    global posX, posY
    posX -= 1
    update()

update()

root.mainloop()