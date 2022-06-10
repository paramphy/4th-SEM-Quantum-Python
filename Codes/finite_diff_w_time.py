import numpy as np

import matplotlib.pyplot as plt


L = 0.1  

n = 10      

T0 = 20  

T1s = 40 

T2s = 20 

dx = L/n

alpha = 0.000000054713  

t_final = 1800  

dt = 60


x = np.linspace(dx/2, L-dx/2, n)



T = np.ones(n)*T0

dTdt = np.empty(n)



t = np.arange(0, t_final, dt)


for j in range(1,len(t)):

    plt.clf()

    for i in range(1, n-1):

        dTdt[i] = alpha*(-(T[i]-T[i-1])/dx**2+(T[i+1]-T[i])/dx**2)

    dTdt[0] = alpha*(-(T[0]-T1s)/dx**2+(T[1]-T[0])/dx**2)

    dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2+(T2s-T[n-1])/dx**2)

    T = T + dTdt*dt

    plt.figure(1)

    plt.plot(x,T)

    plt.axis([0, L, 0, 50])

    plt.xlabel('Distance (m)')

    plt.ylabel('Temperature (C)')

    plt.show()

    plt.pause(0.01)