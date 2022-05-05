# 3.d^x/dt^2+lambda dx/dt+kx=0
# Solve the above differential equation

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

k = 1.0
lam = 0.4
F = lambda t, u: np.dot(np.array([[0, 1], [0, (-k * u[0] - lam * u[1]) / u[1]]]), u)
x0, y0 = 0, 1
t_eval = np.linspace(0, 20, 100)
sol = solve_ivp(F, [0, 20], [x0, y0], t_eval=t_eval)
plt.title("Damped Harmonic Oscillator")
plt.xlabel("time(t)")
plt.plot(sol.t, sol.y[0], label="Position")
plt.plot(sol.t, sol.y[1], label="Velocity")
plt.legend()
plt.show()
