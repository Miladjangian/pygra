# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])
from pygra import geometry
from pygra import topology
g = geometry.honeycomb_lattice()
h = g.get_hamiltonian()
h.add_rashba(0.3) # Rashba spin-orbit coupling
h.add_zeeman([0.,0.,0.3]) # Exchange field
c = topology.chern(h)
print("Chern number is ",c)

