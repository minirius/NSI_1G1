import numpy as np
from pypoly import Polynomial
import matplotlib.pyplot as plt

x, X = 10, [[0, 60], [1, 10], [2, 40], [3, 20], [4, 80], [5, 0], [6, 30], [7, 70], [8, 40], [9, 90]]
order = len(X)

def ReadFile():
    #Read the coef
    global x, X
    x, X = 10, [[0, 60], [1, 10], [2, 40], [3, 20], [4, 80], [5, 0], [6, 30], [7, 70], [8, 40], [9, 90]]
    return True
    None

def StoreFile():
    #Store only the coef
    return True
    None

def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {o}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y

def ShowGraphic(coefficients):
    for i in X:
        plt.scatter(i[0], i[1], c='k')
    x = np.linspace(0, len(X), 100)
    plt.plot(x, PolyCoefficients(x, coefficients))
    plt.show()

def FindEquation():
    equations = np.array([[point[0] ** i for i in range(order)] for point in X])
    values = np.array([point[1] for point in X])
    coefficients = np.linalg.solve(equations, values)
    print('coefficients', list(coefficients))
    p = Polynomial(*coefficients)
    return p


X = 1
eq = 60 - 2854.74 * X + 7053.26 * X**2 - 6903.5 * X**3 + 3537.7 * X**4 - 1051.86 * X**5 + 187.896 * X**6 - 19.873 * X**7 + 1.14633 * X**8 - 0.0277778 * X**9
print(round(eq))
