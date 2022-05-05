"""
Solving second-order ordinary differential equations by the Numerov method

"""
import numpy as np
import matplotlib.pyplot as plt

delta_x = 0.005
xL0, xR0 = 0, 1
Nx = int((xR0 - xL0) / delta_x)

k2 = np.zeros([Nx + 1])
k2[:] = 4 * np.pi

y = np.zeros([Nx])

# Initial conditions
y[0] = 1
y[1] = 1  # y'(0) = (y[1]-y[0])/delta_Evaluate by forward difference with x


def Numerov(N, delta_x, k2, u):  # Development by the Numerov method
    b = (delta_x ** 2) / 12.0
    for i in range(1, N - 1):
        u[i + 1] = (2 * u[i] * (1 - 5 * b * k2[i]) - (1 + b * k2[i - 1]) * u[i - 1]) / (
            1 + b * k2[i + 1]
        )


Numerov(Nx, delta_x, k2, y)  # Numerov method solution

# for plot
X = np.linspace(xL0, xR0, Nx)
y_exact = np.cos(2 * np.sqrt(np.pi) * X)
plt.plot(X, y, "o", markersize=2, label="Numerov")
plt.plot(X, y_exact, "-", color="red", markersize=0.5, label="Exact")
plt.legend(loc="upper right")
plt.xlabel("X")  # x-axis label
plt.ylabel("Y")  # y-axis label

plt.show()
