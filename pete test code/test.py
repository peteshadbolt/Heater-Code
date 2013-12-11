import numpy as np
from qy.simulation import linear_optics as lo

# First Let's load up a device from a JSON definition file:
w=lo.quantum_walk(5)
print w.hamiltonian