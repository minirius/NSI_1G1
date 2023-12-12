import numpy as np
import matplotlib.pyplot as plt
import random

class LagrangePoly:
    def __init__(self, X, Y):
        self.n = len(X)
        self.X = np.array(X)
        self.Y = np.array(Y)

    def basis(self, x, j):
        b = [(x - self.X[m]) / (self.X[j] - self.X[m])
             for m in range(self.n) if m != j]
        return np.prod(b, axis=0) * self.Y[j]

    def interpolate(self, x):
        b = [self.basis(x, j) for j in range(self.n)]
        return np.sum(b, axis=0)


Y  = [random.randint(0, 100) for i in range(50)]
X  = [i for i in range(len(Y))]

plt.scatter(X, Y, c='k')

lp = LagrangePoly(X, Y)

xx = np.arange(0, max(X)*20+1) / 20

for i in range(len(X)):
    plt.plot(xx, lp.basis(xx, i), linestyle=':')
XY = np.stack((lp.interpolate(xx),xx))
plt.plot(xx, lp.interpolate(xx))
plt.plot(XY[1], XY[0], linestyle=":")
print(XY)
plt.show()