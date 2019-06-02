from Bio import Phylo

import networkx
import igraph
from igraph import *

from graphviz import Digraph
from pygraphviz import *

# import pydot

newick = "(ta:0.145313, (pa:0.142047, (ml:0.165216, (hi:0.210634, (mr:0.146529, (ne:0.102035, (sa:0.105757, (gu:0.110000, bn:0.117400):0.013043):0.025140):0.016884):0.016691):0.019324):0.013033):0.005953, te:0.147087);"

Tree = Phylo.read("small.newick",'newick')


def clade_names_fix(tree):
    	for idx, clade in enumerate(tree.find_clades()):
            if not clade.name:
                clade.name="id_%s"%(idx)

clade_names_fix(Tree)

G = Phylo.to_networkx(Tree)

# networkx.write_graphml(G, 'small.graphml')
A = networkx.nx_pydot.to_pydot(G)
A.render('a.gv',view=True)

A.write_png('a.png')
