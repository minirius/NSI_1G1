from turtle import *

reset()
n = int(input("Tours spirale ? "))
for i in range(2 * n):
    width(i)
    circle(i*i, 180)
exitonclick()