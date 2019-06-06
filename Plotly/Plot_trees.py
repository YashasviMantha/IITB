from Bio import Phylo
# from pygraphviz import *
# from networkx.drawing import nx_agraph

tree = Phylo.read("Plotly/small.newick",'newick')

Phylo.draw_graphviz(tree,prog='dot')
