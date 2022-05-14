import numpy as np
from matplotlib import pyplot as plt
from scipy.special import jv

x = np.linspace(0, 10, 1000)
y = jv(0, x)
# print(y)
plt.title("Bassel functions")
plt.xlabel("x")
plt.ylabel("$J_n$")
plt.plot(x, jv(0, x), label="n = 0")
plt.plot(x, jv(1, x), label="n = 1")
plt.plot(x, jv(2, x), label="n = 2")
plt.plot(x, jv(3, x), label="n = 3")
plt.plot(x, jv(4, x), label="n = 4")
plt.legend()
plt.show()
