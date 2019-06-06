import math
from Bio import Phylo
import igraph


tree = Phylo.read("work/NLP/Plotly/small.newick",'newick')


from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

inner_node_color ='rgb(204, 204, 205)'# a color for edges and internal nodes

#a dictionary to color the nodes by key
color_dict={'hi': 'rgb(230, 0, 230)',
            'mr': 'rgb(128, 128, 255)',
            'pa': 'rgb(0, 204, 0)',
            'bn': 'rgb(51, 102, 255)',
            'gu': 'rgb(178,223,138)',
            'sa': 'rgb(255, 0, 255)',
            'ta': 'rgb(230, 0, 0)',
            'ml': 'rgb(255, 255, 0)',
            'ne': 'rgb(255, 105, 180)',
            'te': 'rgb(255, 105, 056)'
           }

def set_node_color(label):

    node_color = 'blue'#default color
    for Key in color_dict:
        if Key in label:
            node_color = color_dict[Key]
    return node_color


def get_tree():
    #biopython-extract the unrooted  tree
    aln = AlignIO.read('agc.aln', 'clustal')
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(aln)
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(dm)
    return tree



def convert_to_igraph(tree):
    #Convert a Biopython Tree object to an igraph Graph.
    def add_edge(graph, node1, node2):
        graph.add_edge(node1.name, node2.name)


    def build_subgraph(graph, top):
        """Traverse  the Tree, and retrieve  graph edges and nodes."""
        for clade in top:
            graph.add_vertex(name=clade.root.name)
            add_edge(graph, top.root, clade.root)
            build_subgraph(graph, clade)

    if tree.rooted:
        G = igraph.Graph(directed=True)
    else:
        G = igraph.Graph()

    if (str(tree.root) != None):
        name = tree.root
    else:
        name = 'aaa'
    G.add_vertex(name)
    build_subgraph(G, tree.root)
    return G


G = convert_to_igraph(tree)

# for i in range(len(G.vs)):


# node_colors=[inner_node_color if 'Inner'  in v['name'] else set_node_color(v['name']) for v in G.vs]



V =[v.index for v in G.vs]
Edges=[e.tuple   for e in G.es]

labels=[v['name']   for v in G.vs]
for i in range(len(labels)):
    if(labels[i] == None):
        labels[i] = str(i)
display_labels=['' if 'Inner' in label else label for label in labels]
node_size=[1 if d_label == '' else 12 for d_label in display_labels]


layt=G.layout('rt')
N=len(layt)# N is equal to len(V)=len(G.vs)
N

# PLOTLY STUFF::::
import plotly.plotly as py
from plotly.graph_objs import *


Xn=[layt[k][0] for k in range(N)]
Yn=[layt[k][1] for k in range(N)]

for i in range(len(Xn)):
    if(Xn[i] == None):
        Xn[i] = 0


for i in range(len(Yn)):
    if(Yn[i] == None):
        Yn[i] = 0

Xe=[]
Ye=[]
for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]

for i in range(len(Xe)):
    if(Xe[i] == None):
        Xe[i] = 0
for i in range(len(Ye)):
    if(Ye[i] == None):
        Ye[i] = 0

trace1=Scatter(x=Xe,
               y=Ye,
               mode='lines',
               line=Line(color=inner_node_color, width=1),
               hoverinfo='none'
               )
trace2=Scatter(x=Xn,
               y=Yn,
               mode='markers',
               name='',
               marker=Marker(symbol='square-dot',
                             size=node_size,
                            #  color=node_colors,
                             line=Line(color='rgb(50,50,50)', width=0.5)
                             ),
               text=display_labels,
               hoverinfo='text'
               )

axis=dict(showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

layout = Layout(
         title="Unrooted tree from sequence alignments,<br> with Biopython, Igraph and  Plotly",
         width=800,
         height=800,
         showlegend=False,
         xaxis=XAxis(axis),
         yaxis=YAxis(axis),

     margin=Margin(
        t=100
    ),
    hovermode='closest',
     annotations=Annotations([
           Annotation(
           showarrow=False,
            text="Data source: <a href='http://kinase.com/human/kinome/groups/agc.aln'> [1]</a>",
            xref='paper',
            yref='paper',
            x=0.2,
            y=-0.1,
            xanchor='left',
            yanchor='bottom',
            font=Font(
            size=14
            )
            )
        ]),

      )

data=Data([trace1,trace2])
fig=Figure(data=data, layout=layout)

py.sign_in('YashasviMantha', 'yU2bvmTfj1abQSsF2WbB')
py.iplot(fig, filename='unrooted-tree')