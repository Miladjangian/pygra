
import sys
sys.path.append("../../../pygra")  # add pygra library

import geometry
import topology
import klist

g = geometry.diamond_lattice_minimal()
h = g.get_hamiltonian(has_spin=True)
h.intra *= 1.3
h.add_kane_mele(0.05)
import kdos
kdos.surface(h,operator=None)