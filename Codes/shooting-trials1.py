import numpy as np
from matplotlib import pyplot as plt

from scipy.integrate import solve_ivp

F = lambda t,s: np.dot(np.array([[1,0],[0,-9.8/s[1]]]),s)

y0 = 0
v0 = float(input("Input the guess value of initial velocity: "))
t_eval = np.linspace(0,5,1000)
sol = solve_ivp(F, [0,5],[y0,v0],t_eval=t_eval)
plt.figure(figsize=(10,8))
plt.plot(sol.t, sol.y[0])
plt.plot(5,50,"ro")
plt.show()