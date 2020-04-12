#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import networkx as nx
import plotly.graph_objs as go

# In[2]:
theme = 'fp_report'
df = pd.read_csv(theme + '.csv')
#carac = pd.read_csv(theme + '_weights.csv')

df = df[df.Occurences > 0]

# In[3]:
df.head()

# In[4]:
G = nx.from_pandas_edgelist(df, 'Ground_Truth', 'Prediction', create_using=nx.DiGraph())

# In[5]:
pos = nx.spring_layout(G, k=0.5, iterations=50)
#pos

# In[6]:
for n, p in pos.items():
    G.nodes[n]['pos'] = p

# In[7]:
G.nodes(data=True)

# In[8]:
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]['pos']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])

# In[9]:


labels = []
hover_info = []
marker_color = []
for node, adjacencies in enumerate(G.adjacency()):
    marker_color += tuple([len(adjacencies[1])])
    node_info = adjacencies[0] + ', # of connections: ' + str(len(adjacencies[1]))
    node_label = adjacencies[0]
    labels += tuple([node_label])
    hover_info += tuple([node_info])
labels, hover_info, marker_color

# In[10]:


colorscale = 'picnic'
node_trace = go.Scatter(
    x=[],
    y=[],
    text=labels,
    mode='markers+text',
    hovertext=hover_info,
    hoverinfo='text',
    textfont=dict(color='black'),
    marker=dict(
        showscale=True,
        colorscale=colorscale,
        reversescale=True,
        color=marker_color,
        size=15,
        colorbar=dict(
            thickness=10,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=0)))

for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])

# In[11]:


import plotly.io as pio

fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 5], mode="lines+text", name="Lines",
                           text=["Text A", "Text B", "Text C", "D"], textposition="top center"))
fig.update_layout(title_text='hello world')
fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[3, 3, 3],
    mode="lines+text",
    name="Lines and Text",
    text=["Text G", "Text H", "Text I"],
    textposition="top center"
))

pio.show(fig)
# In[12]:


fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title={
                        'text': theme + " Association Graph",
                        'y': 0.97,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    titlefont=dict(size=27),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20, l=5, r=5, t=40),
                    annotations=[dict(
                        text=theme + " Dataset",
                        showarrow=False,
                        xref="paper", yref="paper")],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

# iplot(fig)
pio.show(fig)

# In[13]:


G.edges()

# In[14]:


# [edge_trace, node_trace]
