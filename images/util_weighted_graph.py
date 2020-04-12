import networkx as nx
import pylab
import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

G = nx.DiGraph(directed=True)

input_file = 'regular_output.csv'

filtered_data_frame = pd.read_csv(input_file)

for _, row in filtered_data_frame.iterrows():
    row_tuple = (row.Ground_Truth, row.Prediction)
    G.add_edges_from([row_tuple], weight=row.Occurences)
    print('{} - {} - {}'.format(row.Ground_Truth, row.Prediction, row.Occurences))

edge_labels = dict([((u, v,), d['weight'])
                    for u, v, d in G.edges(data=True)])

edge_colors = ['blue' for edge in G.edges()]

pos = nx.spring_layout(G)
# nx.draw_networkx(G, pos, with_labels=True)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# nx.draw(G, pos, node_size=2000, edge_color=edge_colors, edge_cmap=plt.cm.Reds)

# set defaults
G.graph['graph'] = {'rankdir': 'TD'}
G.graph['node'] = {'shape': 'circle'}
G.graph['edges'] = {'arrowsize': '4.0', 'edge_labels': 'True'}

nx.set_edge_attributes(G, {(e[0], e[1]): {'label': e[2]['weight']} for e in G.edges(data=True)})
D = to_agraph(G)
D.node_attr.update(color='blue', style='filled', fillcolor='yellow')
D.edge_attr.update(color='blue', arrowsize=1)
pos = D.layout('dot')
D.draw('abcd.png')

# pylab.show()
