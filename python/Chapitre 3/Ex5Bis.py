import random
from turtle import *

bateau = (random.randint(0, 9), random.randint(0, 4))

grille = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def render():
    clearstamps()  
    for i, ligne in enumerate(grille):
        for j, case in enumerate(ligne): 
            color('Black', "")
            goto(j*20, i*20)
            stamp()
        
def left():
    None
def right():
    None
def Up():
    None
def Down():
    None

def space():
    None

tracer(True)
hideturtle()
up()
shape("square")
speed(9)
render()

LIENS = [(right, "Right"), (left, "Left"), (Down, "Up"), (Up, "Down"), (space, "space")]
for action, touche in LIENS:
    onkeypress(action, touche)
listen()