import numpy
import math
from skbio.tree import nj
from skbio import DistanceMatrix
from numpy import genfromtxt
import argparse
from Bio import Phylo
import networkx
# from networkx.drawing import nx_agraph
import pylab
# from matplotlib import pyplot
# import pydot
from networkx.drawing import nx_agraph
from networkx.drawing.nx_agraph import graphviz_layout
from pygraphviz import *
# parser = argparse.ArgumentParser(description = 'Distance Martix')
# parser.add_argument('-dm', metavar='DM_file',type=str,help='File name which containg the DM')
# parser.add_argument('-string', metavar='NW_file',type=str,help="File to store the NWS")
# parser.add_argument('-tree', metavar='Tree_file',type=str,help='File to storing the tree in ASCII')

# distance_matrix_file = 'nope'
# nws_file = 'nope'
# tree_file = 'nope'

# args = parser.parse_args()

# if(distance_matrix_file != 'nope'):
#     distance_matrix_file = args.DM_file
# else:
#     distance_matrix_file = 'CLWE_angular.csv'
# if(nws_file != 'nope'):
#     nws_file = args.NWS_file
# else:
#     nws_file = 'output_data.txt'
# if(tree_file != 'nope'):
#     tree_file = args.Tree_file
# else:
#     tree_file = 'tree.txt'


distance_matrix_file = 'work/NLP/Trees/CLWE_angular.csv'
nws_file = 'work/NLP/Trees/output_data_new.txt'
tree_file = 'work/NLP/Treestree.txt'



# Finding IDS
file = open(distance_matrix_file,'rt')
data = file.readlines()
data = list(data)
ids = []
for i in range(len(data)-1):
    row = data[i+1]
    row = row.split(',')
    ids.append(row[0])

my_data = genfromtxt(distance_matrix_file, delimiter=',')


my_data = my_data.tolist()
del my_data[0]
for i in range(len(my_data)):
    del my_data[i][0]

for i in range(len(my_data)):
    for j in range(len(my_data[i])):
        if(math.isnan(my_data[i][j])):
            my_data[i][j] = 0

my_data = numpy.array(my_data)

data = my_data.T + my_data

for i in data:
    for j in i:
        print(j,end = '   ')
    print()

dm = DistanceMatrix(data,ids)

tree = nj(dm,disallow_negative_branch_length=False)
print(tree.ascii_art())

tree_file = open(tree_file,'w+')
tree_file.write(tree.ascii_art())
tree_file.close()

nws = nj(dm, result_constructor=str)
print(nws)

nws_file_l = open(nws_file,'w+')
nws_file_l.write(nws)
nws_file_l.close()


bio_tree = Phylo.read("work/NLP/Trees/output_data.txt",'newick')

tree_net = Phylo.to_networkx(bio_tree)
# networkx.graphviz_layout = networkx.drawing.nx_agraph.pydot_layout

# networkx.draw(tree_net,pos=networkx.spring_layout(tree_net))
# networkx.draw(tree_net)
# matplotlib.plot()
# pyplot.draw()
# pyplot.show()

# graphviz_layout = nx_agraph.pydot_layout

H = networkx.nx_agraph.to_agraph(tree_net)
H.layout()
H.draw('a.ph')
# Phylo.draw_graphviz(H,prog='dot')
# pylab.show()
# pylab.savefig('apaf.png')