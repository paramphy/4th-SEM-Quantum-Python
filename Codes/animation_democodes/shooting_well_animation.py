import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import brentq
from matplotlib.animation import FuncAnimation


def V(x):

    L = 1
    if abs(x) > L:
        return 0
    else:
        return Vo


def plotpotential(x):
    pot = []
    for i in x:
        pot.append(V(i))
    return np.array(pot)


def SE(psi, x):
    state0 = psi[1]
    state1 = 2.0 * (V(x) - E) * psi[0]
    return np.array([state0, state1])


def Wave_function(energy):

    global psi
    global E
    E = energy
    psi = odeint(SE, psi0, x)
    return psi[-1, 0]


def find_all_zeros(x, y):

    all_zeros = []
    s = np.sign(y)
    for i in range(len(y) - 1):
        if s[i] + s[i + 1] == 0:
            zero = brentq(Wave_function, x[i], x[i + 1])
            all_zeros.append(zero)
    return all_zeros


# data which the line will
# contain (x, y)


def init():
    line.set_data([], [])
    return (line,)


def animate(i):
    x = np.linspace(-b, b, N)
    lines = []
    # plots a sine graph
    # for E in E_zeros:
    Wave_function(E_zeros[-2])
    line.set_data(
        x,
        E_zeros[-2] + (psi[:, 0] / np.max(psi[:, 0])) * np.cos(E_zeros[-2] * i * 0.001),
    )
    # y = np.sin(2 * np.pi * (x - 0.01 * i))*np.exp(-i*0.003)
    # line.set_data(x, y)

    return (line,)


# initializing a figure in
# which the graph will be plotted

N = 1000
psi = np.zeros([N, 2])
psi0 = np.array([0, 1])
Vo = -20
E = 0.0
b = 2
x = np.linspace(-b, b, N)


def main():

    en = np.linspace(0, Vo, 100)

    psi_b = []

    for e in en:
        psi_b.append(Wave_function(e))

    global E_zeros
    E_zeros = find_all_zeros(en, psi_b)

    print("Energy of the bound states")
    # print(E_zeros, psi_b)
    for E in E_zeros:
        print("Energy = ", E)
        plt.annotate("Energy= " + str(E), [E, 0])
    plt.plot(en / Vo, psi_b)
    plt.scatter(np.array(E_zeros) / Vo, np.zeros_like(E_zeros), label="Energies")
    plt.xlabel("Energy,$E/V_0$")
    plt.ylabel("$\Psi(x=b)$")
    plt.grid()
    plt.show()

    for E in E_zeros:
        Wave_function(E)

        plt.plot(x, E + (psi[:, 0] / np.max(psi[:, 0])), label="E = %.2f" % E)
    plt.plot(x, plotpotential(x), label="Potential")
    plt.grid()
    plt.title("Wave function")
    plt.xlabel("x")
    plt.ylabel("Energy")
    plt.legend()
    plt.show()


# if __name__ == "__main__":
main()
fig = plt.figure()

# marking the x-axis and y-axis
axis = plt.axes(xlim=(-2, 2), ylim=(E_zeros[-2] - 1, E_zeros[-2] + 1))

# initializing a line variable
(line,) = axis.plot([], [], lw=3)
anim = FuncAnimation(fig, animate, init_func=init, frames=2000, interval=0.1, blit=True)
plt.show()
