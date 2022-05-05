import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

F = lambda t, s: np.dot(np.array([[0, 1], [0, -9.8 / s[1]]]), s)

y0 = 0
v0 = np.linspace(30, 40, 21)

t_eval = np.linspace(0, 5, 100)
plt.figure(figsize=(10, 8))
for v in v0:
    sol = solve_ivp(F, [0, 5], [y0, v], t_eval=t_eval)

    plt.plot(sol.t, sol.y[0])

plt.plot(5, 50, "ro")
plt.xlabel("time (s)")
plt.ylabel("altitude (m)")
plt.title(f"first guess v={v0} m/s")
plt.show()
