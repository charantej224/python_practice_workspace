import networkx as nx
import pylab
import pandas as pd
import matplotlib.pyplot as plt

G = nx.DiGraph(directed=True)

filtered_data_frame = pd.read_csv('filtered.csv')

for _, row in filtered_data_frame.iterrows():
    row_tuple = (row.Ground_Truth, row.Prediction)
    G.add_edges_from([row_tuple], weight=row.Occurences)
    print('{} - {} - {}'.format(row.Ground_Truth, row.Prediction, row.Occurences))

'''
G.add_edges_from([('aeroplane', 'person')], weight=3)
G.add_edges_from([('aeroplane', 'pottedplant')], weight=3)
G.add_edges_from([('aeroplane', 'train')], weight=3)
G.add_edges_from([('bicycle', 'chair')], weight=3)
G.add_edges_from([('bicycle', 'motorbike')], weight=3)
'''
'''
G.add_edges_from([('A', 'B'), ('C', 'D'), ('G', 'D')], weight=1)
G.add_edges_from([('A', 'C'), ('A', 'D')], weight=7)
G.add_edges_from([('D', 'A'), ('D', 'E'), ('B', 'D'), ('D', 'E')], weight=2)
G.add_edges_from([('B', 'C'), ('E', 'F')], weight=3)
G.add_edges_from([('C', 'F')], weight=4)
'''

edge_labels = dict([((u, v,), d['weight'])
                    for u, v, d in G.edges(data=True)])

edge_colors = ['blue' for edge in G.edges()]

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw(G, pos, node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
pylab.show()
