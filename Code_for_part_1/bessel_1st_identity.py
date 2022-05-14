import numpy as np
from matplotlib import pyplot as plt
from scipy.special import jv


def identity(x, order):
    return np.average(
        np.append(x[1:] * np.diff(jv(order, x), n=1), [1], 0)
        + order * jv(order, x)
        - x * jv(order - 1, x)
    )


x = np.linspace(0, 100, 10000)
for n in range(1, 1000):
    plt.scatter(n, identity(x, n))
plt.xlabel("Order(n)")
plt.ylabel("Avg value of the identity")
plt.title("$xJ'_n(x)+nJ_n(x)=xJ_{n-1}(x)$")
plt.grid()
plt.legend()
plt.show()
