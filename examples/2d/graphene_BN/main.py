
import sys
import os
sys.path.append(os.environ["PYGRAROOT"])  # add pygra library

import specialgeometry

# the following input numbers are the number of replicas required
# by each lattice to be commensurate
g = specialgeometry.mismatched_lattice(11,10)

g.write()

from specialhopping import twisted_matrix

h = g.get_hamiltonian(is_sparse=True,has_spin=False,is_multicell=False,
     mgenerator=twisted_matrix(ti=0.4,lambi=5.0))

def fm(r):
    if r[2]<0.0: return 3.5
    return 0.0
h.add_sublattice_imbalance(fm)

h.get_bands(nk=1000)


