import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import newton


def leftfunc(x):
    return x * np.tan(x)


def rightfunc(x):
    return np.sqrt(50 - x ** 2)


def your_funcs(x):

    f = leftfunc(x) - rightfunc(x)
    return f


x = np.linspace(0, 10, 1000)
plt.scatter(x, leftfunc(x))
plt.plot(x, rightfunc(x))
plt.axis([0, 10, 0, 10])
plt.show()

initial_guess = float(input("Input the initial guess: "))
sol2 = newton(your_funcs, initial_guess)
print(sol2)
