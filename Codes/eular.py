import numpy as np
from matplotlib import pyplot as plt

a = 10  # a(Amplitude of external force)
(m, gm2, k) = (30, 5, 1)  # m,2Γ,k
omg = np.pi  # ω


def f(t, x):
    f0 = x[1]
    f1 = -(gm2 / m) * x[1] - (k / m) * x[0] + (a / m) * np.sin(omg * t)
    return np.array([f0, f1])


dt = 0.01


def f_D_eular(t, x):
    return (t + dt, x + f(t, x) * dt)


def main():
    (t0, x0) = (0, np.array([1, 0]))
    t1 = 100
    (t, x) = (t0, x0)
    y = []
    t2 = []
    while t < t1:
        # print(t,x[0])
        (t, x) = f_D_eular(t, x)
        y.append(x)
        t2.append(t)
    y = np.array(y)
    t2 = np.array(t2)
    plt.plot(t2, y[:, 0], label="Position")
    plt.plot(t2, y[:, 1], label="Velocity")
    plt.xlabel("time(s)")
    plt.legend()
    plt.grid()
    plt.show()


if "__name__" == "__main__":
    main()
