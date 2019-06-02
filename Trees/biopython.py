from io import StringIO
from Bio import Phylo

import plotly.plotly as py
from plotly.graph_objs import *

import igraph
from igraph import *

treedata = "(ta:0.145313, (pa:0.142047, (ml:0.165216, (hi:0.210634, (mr:0.146529, (ne:0.102035, (sa:0.105757, (gu:0.110000, bn:0.117400):0.013043):0.025140):0.016884):0.016691):0.019324):0.013033):0.005953, te:0.147087);"

handle = StringIO(treedata)
tree = Phylo.read(handle, "newick")


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
    G.add_vertex(name=str(tree.root))
    build_subgraph(G, tree.root)
    return G

G=convert_to_igraph(tree)

# plotly code
inner_node_color ='rgb(204, 204, 205)'# a color for edges and internal nodes

color_dict={'hi': 'rgb(230, 0, 230)',
            'mr': 'rgb(128, 128, 255)',
            'bn': 'rgb(0, 204, 0)',
            'gu': 'rgb(51, 102, 255)',
            'pa': 'rgb(178,223,138)',
            'ne': 'rgb(255, 0, 255)',
            'te': 'rgb(230, 0, 0)',
            'ta': 'rgb(255, 255, 0)',
            'sa': 'rgb(255, 105, 180)',
            'ml': 'rbg(255,60,100)'
           }


def set_node_color(label):

    node_color = 'blue'#default color
    for Key in color_dict:
        if Key in label:
            node_color = color_dict[Key]
    return node_color


V =[v.index for v in G.vs]
Edges=[e.tuple   for e in G.es]


node_colors=[set_node_color(v['name']) for v in G.vs]

labels=[v['name']   for v in G.vs]
display_labels=['' if 'Inner' in label else label for label in labels]
node_size=[1 if d_label == '' else 12 for d_label in display_labels]

layt=G.layout('kk')
N=len(layt)# N is equal to len(V)=len(G.vs)

Xn=[layt[k][0] for k in range(N)]
Yn=[layt[k][1] for k in range(N)]

Xe=[]
Ye=[]
for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]


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
               marker=Marker(symbol='dot',
                             size=node_size,
                             color=node_colors,
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

data=Data([trace1, trace2])
fig=Figure(data=data, layout=layout)

fig['layout'].update(annotations=make_annotations(position, v_label))
py.iplot(fig, filename='unrooted-tree')
