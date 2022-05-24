from scipy import *
from scipy import integrate
from scipy import optimize
import numpy as np
from matplotlib import pyplot as plt


def Numerov(f, x0, dx, dh):
    """Given precomputed function f(x), solves for x(t), which satisfies:
    x''(t) = f(t) x(t)
    """
    x = np.zeros(len(f))
    x[0] = x0
    x[1] = x0 + dh * dx

    h2 = dh ** 2
    h12 = h2 / 12.0

    w0 = x0 * (1 - h12 * f[0])
    w1 = x[1] * (1 - h12 * f[1])
    xi = x[1]
    fi = f[1]
    for i in range(2, len(f)):
        w2 = 2 * w1 - w0 + h2 * fi * xi  # here fi=f1
        fi = f[i]  # fi=f2
        xi = w2 / (1 - h12 * fi)
        x[i] = xi
        w0 = w1
        w1 = w2
    return x


def fSchrod(En, R):
    return 2*((-np.exp(-R) / R) - En)


def ComputeSchrod(En, R):
    "Computes Schrod Eq."
    f = fSchrod(En, R[::-1])
    ur = Numerov(f, 0.0, -1e-7, -R[1] + R[0])[::-1]
    norm = integrate.simps(ur ** 2, x=R)
    return ur * 1 / np.sqrt(abs(norm))


def Shoot(En, R):
    ur = ComputeSchrod(En, R)
    f0 = ur[0]
    f1 = ur[1]
    f_at_0 = f0 + (f1 - f0) * (0.0 - R[0]) / (R[1] - R[0])
    return f_at_0


def FindBoundStates(R, nmax, Esearch):
    n = 0
    Ebnd = []
    u0 = Shoot(Esearch[0], R)
    for i in range(1, len(Esearch)):
        u1 = Shoot(Esearch[i], R)
        if u0 * u1 < 0:
            Ebound = optimize.brentq(
                Shoot, Esearch[i - 1], Esearch[i], xtol=1e-16, args=(R)
            )
            Ebnd.append(Ebound)
            if len(Ebnd) > nmax:
                break
            n += 1
            print("Found bound state at E=%14.9f " % (Ebound))
        u0 = u1

    return Ebnd


Esearch = -2 / np.arange(1, 200, 0.2) ** 2


R = np.linspace(1e-8, 100, 2000)

nmax = 10

Bnd = FindBoundStates(R,nmax, Esearch)
rho = np.zeros(len(R))
for En in Bnd:
    ur = ComputeSchrod(En, R)
    
    plt.plot(R, ur * ur, label="E = " + str(round(En, 4)))

plt.legend()
plt.show()
