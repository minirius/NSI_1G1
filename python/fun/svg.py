import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.backend_bases import MouseButton 
import cairo 
from tkinter import filedialog
import os


POINTS = []
fig, ax = plt.subplots()

def bernstein(v, n, x):
    binomial = (math.factorial(n))/(math.factorial(v)*math.factorial(n-v))
    return binomial*(x**v)*((1-x)**(n-v))

def bezier_x(n, x):
    total = 0
    for v in range(0, n):
        total += bernstein(v, n-1, x)*POINTS[v][0]
    return total

def bezier_y(n, x):
    total = 0
    for v in range(0, n):
        total += bernstein(v, n-1, x)*POINTS[v][1]
    return total

def update():
    global plot
    x = np.arange(0, 1, .01)

    """colors = ["blue", "red", "black", "yellow", "green", "brown", "purple"]
    for i in range(N+1):
        for j in range(i, N+1):
            ax.plot(x, bernstein(i, j, x), color=colors[i%len(colors)])"""

    N = len(POINTS)
    X = []
    Y = []
    for i in np.arange(0, 1, .01):
        X.append(bezier_x(N, i))
        Y.append(bezier_y(N, i))

    plot, = ax.plot(X, Y, color="blue")

    for point in POINTS:
        ax.scatter(point[0], point[1])


def save(X, Y):
    # creating a SVG surface 
    # here geek is file name & 700, 700 is dimension 

    f = filedialog.asksaveasfile(defaultextension=".svg", filetypes=[("SVG Images", '*.svg')])

    ax.clear()
    plt.axis('off')
    ax.grid(False, which='both')
    
    plot, = ax.plot(X, Y, color="blue")

    plt.savefig(f.name, format="svg", dpi=1200)

    plt.close()
    os.startfile(f.name)


def on_click(event):
    global POINTS
    if event.button is MouseButton.LEFT and event.xdata is not None:
        POINTS.append((event.xdata, event.ydata))

        N = len(POINTS)
        X = []
        Y = []
        for i in np.arange(0, 1, .01):
            X.append(bezier_x(N, i))
            Y.append(bezier_y(N, i))

        plot.set_ydata(Y)
        plot.set_xdata(X)

        for point in POINTS:
            ax.scatter(point[0], point[1])

        fig.canvas.draw()
        fig.canvas.flush_events()

        
    elif event.button is MouseButton.RIGHT and event.xdata is not None:
        POINTS = []
        plot.set_ydata([])
        plot.set_xdata([])

        ax.clear()
        plt.axis([-10, 10, -10, 10])

        update()

        fig.canvas.draw()
        fig.canvas.flush_events()

def on_press(event):
    if event.key == 'enter':
        N = len(POINTS)
        X = []
        Y = []

        for i in np.arange(0, 1, .0001):
            X.append(bezier_x(N, i))
            Y.append(bezier_y(N, i))

        save(X, Y)


plt.axis([-10, 10, -10, 10])
plt.connect('button_press_event', on_click)
plt.connect('key_press_event', on_press)
update()

plt.show()