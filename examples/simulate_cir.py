
from time import time

import numpy as np

from sde import SDE
from simulation.strong.explicit.rk import Order_10 as Platen
from simulation.strong.explicit.taylor import Order_05 as Euler

"""
We begin with the definition of both drift and diffusion functions and define the CIR process.
The order in the function interface does matter - the interface needs to be f(x, t, arguments).
"""

def cir_drift(x, a, b):
    return a * (b - x)


def cir_diffusion(x, c):
    return np.sqrt(x) * c

cir_process = SDE(cir_drift, cir_diffusion, timerange=[0,2])

"""
We now compare the run time of the Euler scheme (a strong Taylor scheme of order 0.5) with
the simple Platen scheme (a strong Taylor scheme of order 1.0). Due to 
more function evaluations, we expect the Euler scheme to be faster but be less precise.
"""

euler_path = np.zeros([100, 2001])
platen_path = np.zeros([100, 2001])
print("Run time estimation for Euler and Platen discretization of an CIR process.")

"""
A dictionary for all parameters is given to the iterators representing the schemes.
"""
parameter = {'a': 2, 'b': 2.5, 'c' : 0.2}
t = time()
for i in range(100):
    tmp = []
    for path in Euler(cir_process, parameter, steps=2000):
        tmp.append(path)
    euler_path[i] = tmp
print("Euler: " + str(time() - t))

t = time()
for i in range(100):
    tmp = []
    for path in Platen(cir_process, parameter, steps=2000):
        tmp.append(path)
    platen_path[i] = tmp
print("Platen: " + str(time() - t))

print('Simulation complete.')