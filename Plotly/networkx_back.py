from Bio import Phylo
import networkx
from networkx.drawing import nx_agraph

import igraph
# networkx.graphviz_layout = nx_agraph.pydot_layout

from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot

# Generating IDs
file = open("work/NLP/Trees/Cosine.csv",'rt')
data = file.readlines()
data = list(data)
ids = []
for i in range(len(data)-1):
    row = data[i+1]
    row = row.split(',')
    ids.append(row[0])


tree = Phylo.read("work/NLP/Plotly/small.newick",'newick')
# tree.rooted = True
# Phylo.draw_ascii(tree)

tree_net = Phylo.to_networkx(tree)

# networkx.write_graphml(tree_net,'graph.gml')

# tree_igr = igraph.read('graph.graphml',format='graphml')

# Phylo.draw_graphviz(tree,prog='dot')

pos = networkx.spring_layout(tree_net)
pos = list(pos.values())

Xn=[pos[k][0] for k in range(len(pos))]
Yn=[pos[k][1] for k in range(len(pos))]

# g = networkx.read_gml("graph.gml")
# g.node


# trace_nodes=dict(type='scatter',
#                  x=Xn,
#                  y=Yn,
#                  mode='markers',
#                  marker=dict(size=28, color='rgb(0,240,0)'),
#                 #  text=labels,
#                  hoverinfo='text')

# Xe=[]
# Ye=[]
# for e in tree_net.edges():
#     Xe.extend([pos[e[0]][0], pos[e[1]][0], None])
#     Ye.extend([pos[e[0]][1], pos[e[1]][1], None])



# trace_edges=dict(type='scatter',
#                  mode='lines',
#                  x=Xe,
#                  y=Ye,
#                  line=dict(width=1, color='rgb(25,25,25)'),
#                  hoverinfo='none'
#                 )

# axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
#           zeroline=False,
#           showgrid=False,
#           showticklabels=False,
#           title=''
#           )
# layout=dict(title= 'My Graph',
#             font= dict(family='Balto'),
#             width=600,
#             height=600,
#             autosize=False,
#             showlegend=False,
#             xaxis=axis,
#             yaxis=axis,
#             margin=dict(
#             l=40,
#             r=40,
#             b=85,
#             t=100,
#             pad=0,

#     ),
#     hovermode='closest',
#     plot_bgcolor='#efecea', #set background color
#     )


# fig = dict(data=[trace_edges, trace_nodes], layout=layout)


# iplot(fig)
