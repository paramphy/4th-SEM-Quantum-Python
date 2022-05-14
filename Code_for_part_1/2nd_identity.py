import numpy as np
from matplotlib import pyplot as plt
from scipy.special import lpmv


def identity(x, order):
    return np.average(
        np.append((1 - x[1:] ** 2) * np.diff(lpmv(0, order, x), n=1), [1], 0)
        + (order + 1) * x * lpmv(0, order, x)
        - (n + 1) * lpmv(0, order + 1, x)
    )


x = np.linspace(-1, 1, 1000)
for n in range(2, 1000):
    plt.scatter(n, identity(x, n))
plt.xlabel("Order(n)")
plt.ylabel("Avg value of the identity")
plt.title("$(1-x^2)P'_n(x)+(n+1)xP_n(x)=(n+1)P_{n+1}(x)$")
plt.grid()
plt.legend()
plt.show()
