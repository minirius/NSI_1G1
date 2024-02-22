import matplotlib.pyplot as plt
from  tkinter import simpledialog
import numpy as np

EQUATION = ""

def f(x): 
    return eval(EQUATION)

def graphique():
    x = np.linspace(-100, 100, 100)

    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    ax.plot(x, f(x), color='red')

    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

EQUATION = simpledialog.askstring("Votre fonction", "Fonction")
graphique()