from tkinter import *
from  tkinter import ttk
import matplotlib.pyplot as plt

print("Talbeau de fonction ")

def equation(x): 
    return 2*x*x - 3*x + 5

root  = Tk()
root.title('Equations')
root.geometry('500x500')
root['bg'] = '#AC99F2'

frame = Frame(root)
frame.pack()

tableau = ttk.Treeview(frame)
tableau['columns'] = ('f(x)')
tableau.column("f(x)",anchor=CENTER,width=80)
tableau.heading("f(x)",text="fx",anchor=CENTER)

inputFrame = Frame(root)
inputFrame.pack()
 
Label(inputFrame,text="Min").grid(row=0,column=0)
minText = Entry(inputFrame)
minText.grid(row=1, column=0)

Label(inputFrame,text="Max").grid(row=0,column=1)
maxText = Entry(inputFrame)
maxText.grid(row=1, column=1)

Label(inputFrame,text="Pas").grid(row=0,column=2)
pasText = Entry(inputFrame)
pasText.grid(row=1, column=2)

def graphique():
    X = []
    Y = []
    for x in range(int(minText.get()), int(maxText.get())+1, int(pasText.get())):
        X.append(x)
        Y.append(equation(x))
    plt.plot(X, Y)
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.show()

def update():
    tableau.delete(*tableau.get_children())
    for x in range(int(minText.get()), int(maxText.get())+1, int(pasText.get())):
        tableau.insert(parent='',index='end',iid=x,text=x, values=(equation(x)))

Button(inputFrame, command=update, text="Voir le tableau").grid(row=2, column=1)
Button(inputFrame, command=graphique, text="Voir le graphique").grid(row=4, column=1)


tableau.pack()
root.mainloop()