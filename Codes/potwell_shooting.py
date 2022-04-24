from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import brentq
import numpy as np
 
def V(x):
    """
    Potential function in the finite square well. Width is L and value is global variable Vo
    """
    L = 1
    if abs(x) > L:
        return 0
    else:
        return Vo
 
def SE(psi, x):
    """
    Returns derivatives for the 1D schrodinger eq.
    Requires global value E to be set somewhere. State0 is first derivative of the
    wave function psi, and state1 is its second derivative.
    """
    state0 = psi[1]
    state1 = 2.0*(V(x) - E)*psi[0]
    return np.array([state0, state1])
 
def Wave_function(energy):
    """
    Calculates wave function psi for the given value
    of energy E and returns value at point b
    """
    global psi
    global E
    E = energy
    psi = odeint(SE, psi0, x)
    return psi[-1,0]
 
def find_all_zeroes(x,y):
    """
    Gives all zeroes in y = Psi(x)
    """
    all_zeroes = []
    s = np.sign(y)
    for i in range(len(y)-1):
        if s[i]+s[i+1] == 0:
            zero = brentq(Wave_function, x[i], x[i+1])
            all_zeroes.append(zero)
    return all_zeroes
 
def find_analytic_energies(en):
    """
    Calculates Energy values for the finite square well using analytical
    model (Griffiths, Introduction to Quantum Mechanics, 1st edition, page 62.)
    """
    z = np.sqrt(2*en)
    z0 = np.sqrt(2*Vo)
    z_zeroes = []
    f_sym = lambda z: np.tan(z)-np.sqrt((z0/z)**2-1)      # Formula 2.138, symmetrical case
    f_asym = lambda z: -1/np.tan(z)-np.sqrt((z0/z)**2-1)  # Formula 2.138, antisymmetrical case
 
    # first find the zeroes for the symmetrical case
    s = np.sign(f_sym(z))
    for i in range(len(s)-1):   # find zeroes of this crazy function
       if s[i]+s[i+1] == 0:
           zero = brentq(f_sym, z[i], z[i+1])
           z_zeroes.append(zero)
    print("Energies from the analyitical model are: ")
    print ("Symmetrical case)")
    for i in range(0, len(z_zeroes),2):   # discard z=(2n-1)pi/2 solutions cause that's where tan(z) is discontinous
        print("%.4f" %(z_zeroes[i]**2/2))
    # Now for the asymmetrical
    z_zeroes = []
    s = np.sign(f_asym(z))
    for i in range(len(s)-1):   # find zeroes of this crazy function
       if s[i]+s[i+1] == 0:
           zero = brentq(f_asym, z[i], z[i+1])
           z_zeroes.append(zero)
    print("(Antisymmetrical case)")
    for i in range(0, len(z_zeroes),2):   # discard z=npi solutions cause that's where ctg(z) is discontinous
        print("%.4f" %(z_zeroes[i]**2/2))
 
N = 1000                  # number of points to take
psi = np.zeros([N,2])     # Wave function values and its derivative (psi and psi')
psi0 = np.array([0,1])   # Wave function initial states
Vo = 20
E = 0.0                   # global variable Energy  needed for Sch.Eq, changed in function "Wave function"
b = 2                     # point outside of well where we need to check if the function diverges
x = np.linspace(-b, b, N)    # x-axis
 
def main():
    # main program        
 
    en = np.linspace(0, Vo, 100)   # vector of energies where we look for the stable states
 
    psi_b = []      # vector of wave function at x = b for all of the energies in en
    for e1 in en:
        psi_b.append(Wave_function(e1))     # for each energy e1 find the the psi(x) at x = b
    E_zeroes = find_all_zeroes(en, psi_b)   # now find the energies where psi(b) = 0 
 
    # Print energies for the bound states
    print("Energies for the bound states are: ")
    for E in E_zeroes:
        print("%.2f" %E)
    # Print energies of each bound state from the analytical model
    find_analytic_energies(en)   
 
    # Plot wave function values at b vs energy vector
    #figure()
    plt.plot(en/Vo,psi_b)
    plt.title('Values of the $\Psi(b)$ vs. Energy')
    plt.xlabel('Energy, $E/V_0$')
    plt.ylabel('$\Psi(x = b)$', rotation='horizontal')
    for E in E_zeroes:
        plot(E/Vo, [0], 'go')
        annotate("E = %.2f"%E, xy = (E/Vo, 0), xytext=(E/Vo, 30))
    plt.grid()
 
    # Plot the wavefunctions for first 4 eigenstates
    for E in E_zeroes[0:4]:
        #Wave_function(E)
        plt.plot(x, psi[:,0], label="E = %.2f"%E)
    plt.legend(loc="upper right")
    plt.title('Wave function')
    plt.xlabel('x, $x/L$')
    plt.ylabel('$\Psi(x)$', rotation='horizontal', fontsize = 15)
    plt.grid()
 
if __name__ == "__main__":
    main()