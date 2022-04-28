import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import brentq


def V(x):

    L = 1
    if abs(x)>L:
        return 0
    else:
        return Vo

def SE(psi,x):
    state0 = psi[1]
    state1 = 2.0*(V(x)-E)*psi[0]
    return np.array([state0,state1])

def Wave_function(energy):

    global psi
    global E
    E = energy
    psi = odeint(SE, psi0,x)
    return psi[-1,0]

def find_all_zeros(x,y):

    all_zeros = []
    s = np.sign(y)
    for i in range(len(y)-1):
        if s[i]+s[i+1]==0:
            zero = brentq(Wave_function,x[i],x[i+1])
            all_zeros.append(zero)
    return all_zeros


N = 1000
psi = np.zeros([N,2])
psi0 = np.array([0,1])
Vo = -20
E = 0.0
b = 2
x = np.linspace(-b,b,N)

def main():

    en = np.linspace(0,Vo,100)

    psi_b = []

    for e in en:
        psi_b.append(Wave_function(e))

    E_zeros = find_all_zeros(en,psi_b)

    print("Energy of the bound states")
    print(E_zeros, psi_b)
    for E in E_zeros:
        print("Energy = ", E)
    plt.plot(en/Vo,psi_b)
    plt.scatter(np.array(E_zeros)/Vo,np.zeros_like(E_zeros))
    plt.xlabel('Energy,$E/V_0$')
    plt.ylabel('$\Psi(x=b)$')
    plt.grid()
    plt.show()

    for E in E_zeros:
        Wave_function(E)
        plt.plot(x,psi[:,0])
    plt.grid()
    plt.title("Wave function")
    plt.xlabel('x, $x/L$')
    plt.ylabel('$\Psi(x)$')
    plt.show()

    

if __name__ =="__main__":
    main()
    