# Add the root path of the pygra library
import os ; import sys ; sys.path.append(os.environ['PYGRAROOT'])

import numpy as np
from pygra import geometry
from pygra import groundstate
from pygra import meanfield
from scipy.sparse import csc_matrix
g = geometry.chain()
g = g.supercell(4)
h = g.get_hamiltonian(has_spin=False) # create hamiltonian of the system
nk = 10
filling = 0.5

scf = meanfield.Vinteraction(h,V1=3.0,nk=nk,filling=filling)
h = scf.hamiltonian # get the Hamiltonian
h.get_bands() # calculate band structure
from pygra import topology
groundstate.hopping(h)
