###############################
# Author : Marius
# Name : Immeuble
#
# Dessine des rues en turtle 
###############################
import turtle
import random
import math

COLORS = ["RoyalBlue", "burlywood1", "Cornflowerblue", "DarkOrange", "DarkSeaGreen1", "lightCyan", "firebrick1", "slateBlue2"]

def trait(x1, y1, x2, y2, pensize=1):
    turtle.pensize(pensize)
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

def rectangle(x, y, w, h, color="white", pensize=1):
    turtle.pensize(pensize)
    turtle.goto(x, y)
    turtle.pendown()
    if(color != "transparent"):
        turtle.fillcolor(color)
        turtle.begin_fill()
    turtle.left(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)
    turtle.setheading(0)
    if(color != "transparent"):
        turtle.end_fill()
    turtle.penup()

def sol(y_sol):
    trait(-400, y_sol, 400, y_sol, pensize=3)

def toit_plat(x, y_sol, niveau, color="black"):
    rectangle(x-80, y_sol+60*niveau, w=160, h=10, color=color)

def toit_triangle(x, y_sol, niveau, color="black"):
    turtle.fillcolor(color)
    turtle.goto(x-80, y_sol+60*niveau)
    turtle.pendown()
    turtle.begin_fill()

    turtle.left(math.atan(40/80)*(180/math.pi))
    turtle.forward(math.sqrt(8000))
    turtle.right(180-2*math.atan(80/40)*(180/math.pi))
    turtle.forward(math.sqrt(8000))
    turtle.left(180+math.atan(40/80)*(180/math.pi))
    turtle.forward(160)
    turtle.setheading(0)

    turtle.end_fill()
    turtle.penup()

def toit(x, y_sol, niveau,):
    if(random.choice([1, 0]) == 1):
        toit_plat(x, y_sol, niveau)
    else:
        toit_triangle(x, y_sol, niveau)

def fenetre(x,y):
    rectangle(x-15, y+20, w=30, h=30, color="azure")

def fenetre_balcon(x, y):
    rectangle(x-15, y, w=30, h=50, color="azure")
    rectangle(x-18, y, w=18*2, h=25, color="transparent", pensize=2)
    for i in range(0, 36, 6):
        rectangle(x-18+i, y, w=6, h=25, color="transparent", pensize=2)

def porte(x, y, couleur="white"):
    if(random.choice([1, 0]) == 1):
        rectangle(x-15, y, w=30, h=55, color=couleur)
    else:
        turtle.fillcolor(couleur)
        turtle.goto(x-15, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.setheading(90)
        turtle.forward(40)
        turtle.setheading(270)
        turtle.circle(15, -180)
        turtle.setheading(270)
        turtle.forward(40)
        turtle.setheading(180)
        turtle.forward(30)
        turtle.end_fill()
        turtle.penup()
        turtle.setheading(0)

def facade(x, y_sol, couleur, niveau):
    None

def rdc(x, y_sol, c_facade, c_porte):
    rectangle(x-70, y_sol, w=140, h=60, color=c_facade)
    place=[0, 0, 1]
    random.shuffle(place)
    for i, element in enumerate(place):
        i+=1
        if element == 0:
            fenetre((x-70)+i*35, y_sol)
        else:
            porte((x-70)+i*35, y_sol, couleur=c_porte)

def etage(x, y_sol, couleur, niveau):
    rectangle(x-70, y_sol+niveau*60, w=140, h=60, color=couleur)
    for i in range(1,4):
        element = random.randint(0, 1)
        if element == 0:
            fenetre((x-70)+i*35, y_sol+niveau*60)
        else:
            fenetre_balcon((x-70)+i*35, y_sol+niveau*60)

def immeuble(x, y_sol):
    global COLORS
    color = random.choice(COLORS)
    COLORS.remove(color)
    color2 = random.choice(COLORS)
    COLORS.remove(color2)
    hauteur = random.randint(3,4)

    rdc(x, y_sol, color, color2)
    for i in range(1, hauteur):
        etage(x, y_sol, color,i)
    toit(x, y_sol, hauteur)

def main():
    turtle.penup()
    turtle.hideturtle()
    turtle.tracer(0)
    turtle.Screen().setup(900, 600)
    SOL = -150
    for i in range(0, 4):
        immeuble(i*200 - 300, SOL)
    sol(SOL)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()