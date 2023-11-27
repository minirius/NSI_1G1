###############################
# Author : Marius
# Name : Immeuble
#
# Dessine des rues en turtle 
###############################
import turtle
import random
import math

def couleur_aleatoire():
    liste_couleur = ["RoyalBlue", "grey20", "green2", "red1", "BlueViolet"]
    return random.choice(liste_couleur)
def trait(x1, y1, x2, y2):
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
    trait(-300, y_sol, 300, y_sol)

def toit_plat(x, y_sol, niveau, color="black"):
    rectangle(x-80, 60*niveau, w=160, h=10, color=color)

def toit_triangle(x, y_sol, niveau, color="black"):
    turtle.fillcolor(color)
    turtle.goto(x-80, 60*niveau)
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
    rectangle(x-15, y+20, w=30, h=30, color="grey")

def fenetre_balcon(x, y):
    rectangle(x-15, y, w=30, h=50, color="grey")
    rectangle(x-18, y, w=18*2, h=30, color="transparent", pensize=2)
    for i in range(0, 36, 6):
        rectangle(x-18+i, y, w=6, h=30, color="transparent", pensize=2)

def porte(x, y, couleur="white"):
    if(random.choice([1, 0]) == 1):
        rectangle(x-15, y, w=30, h=55, color=couleur)
    else:
        rectangle(x-15, y, w=30, h=40, color=couleur)
        turtle.fillcolor(couleur)
        turtle.goto(x-15, y+40)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.circle(15, -180)
        turtle.end_fill()
        turtle.penup()
        turtle.setheading(0)

def facade(x, y_sol, couleur, niveau):
    None

def rdc(x, y_sol, c_facade, c_porte):
    rectangle(x-70, y_sol, w=150, h=60, color=c_facade)
    place = random.shuffle([0, 0, 1])
    i = 1
    for element in place:
        if element == 0:
            fenetre(i*(140/4), y_sol)
        else:
            porte(i*(140/4), y_sol, couleur=c_porte)
        i+=1

def etage(x, y_sol, couleur, niveau):
    None

def immeuble(x, y_sol):
    None

def main():
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(0)

    '''rectangle(0, 0, 140, 60, 'blue')
    fenetre(35, 0)
    #fenetre_balcon(70,0)
    porte(70, 0, 'red')
    fenetre(105, 0)
    toit(70, 0, 1)'''

    rdc(0, 0, "white", "yellow")

    turtle.mainloop()

main()