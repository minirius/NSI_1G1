from turtle import *
reset()
n = int(input(">> "))
for i in range(n):
    forward(100)
    left(360/n)

mainloop()