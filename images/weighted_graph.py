import pandas as pd

import matplotlib.pyplot as plt
import networkx as nx
import pylab

# G = nx.Graph()
G = nx.DiGraph(directed=True)
G = nx.generators.directed.random_k_out_graph(10, 3, 0.5)

correlation_data_frame = pd.read_csv('fp_report.csv')
df_filter = correlation_data_frame[correlation_data_frame.Occurences > 0]

df_filter.to_csv('filtered.csv', index=False)
'''

nodes_truth = df_filter.get('Ground_Truth')
nodes_pred = df_filter.get('Prediction')

nodes_set = set()

for value in nodes_truth:
    nodes_set.add(value)

for value in nodes_pred:
    nodes_set.add(value)

for value in nodes_set:
    G.add_node(value)

print(df_filter)
'''
for index, row in df_filter.iterrows():
    print('{} {} {}'.format(row.Ground_Truth, row.Prediction, row.Occurences))
    # G.add_edge(row.Ground_Truth, row.Prediction, weight=row.Occurences)
    G.add_edges_from([row.Ground_Truth, row.Prediction], weight=row.Occurences)

edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

pos = nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
pylab.show()

# edge_list = [(u, v) for (u, v, d) in G.edges(data=True)]

# weights = nx.get_edge_attributes(G, "weight")

# nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
# nx.draw_networkx_edges(G, pos, edgelist=edge_list, arrowstyle='->', arrowsize=10, edge_cmap=plt.cm.Blues, width=2,with_labels=True)

# Create drawing
# pos = nx.spring_layout(G)  # List of positions of nodes
# weights = nx.get_edge_attributes(G, "weight")  # List of weights
# nx.draw_networkx(G, pos, with_labels=True)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

# plt.title("Basic Graphs with Networkx")
# plt.gcf().canvas.set_window_title("")  # Hide window title

# Display Graph
# plt.axis('off')
##plt.savefig("weighted_graph.png")  # save as png
# plt.show()  # display
