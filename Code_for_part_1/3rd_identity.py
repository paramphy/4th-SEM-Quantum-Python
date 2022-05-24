import numpy as np
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from scipy.special import lpmv
from scipy.integrate import quad


def function(x, n, m):
    return lpmv(0, n, x) * lpmv(0, m, x)


def identity(x, n, m, N=1):

    return (
        (2 * n + 1)
        * quad(
            function,
            -N,
            N,
            args=(n, m),
        )[0]
        / 2
    )


x = np.linspace(-1, 1, 100)
n = np.arange(50)
m = np.arange(50)
x = []
y = []
z = []
fig = plt.figure()

# syntax for 3-D projection
ax = plt.axes(projection="3d")
for i in n:
    for j in m:
        x.append(i)
        y.append(j)
        z.append(identity(x, i, j))

ax.scatter(np.array(x), np.array(y), np.array(z), "green")
ax.set_title("Orthogonality relation")
ax.set_xlabel("n")
ax.set_ylabel("m")
plt.show()
