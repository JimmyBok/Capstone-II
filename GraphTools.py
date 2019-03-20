import numpy as np

def format_dict_of_floats(d):
    return {key: '{0:2.2f}'.format(val) for key, val in d.items()}

def get_num_nodes(adj_list):
    '''Return the number of nodes in a graph represented by an adjacency list.'''
    return len(adj_list)

def adjacency_list_to_matrix(adj_list):
    '''Convert an adjacency list to an adjacency matrix.'''
    n_nodes = len(adj_list)
    M = np.zeros(shape=(n_nodes, n_nodes))
    for vertex, lst in adj_list.items():
        for v in lst:
            M[vertex][v] = 1
    return M

def color_node(G, node_id, color):
    '''Add a filled color attribute to a grph node.'''
    G.node[node_id]['style'] = 'filled'
    G.node[node_id]['fillcolor'] = color

def color_edge(G, edge_id, color):
    '''Color a single edge in a graph.'''
    G.edges[(edge_id[0],edge_id[1])]['color'] = color

def color_nodes(G, node_list, color):
    for node in node_list:
        color_node(G, node, color)

def color_edges(G, edge_list, color):
    for edge in edge_list:
        color_edge(G, edge, color)

def label_nodes(G, labeling_dict):
    for node, label in labeling_dict.items():
        G.node[node]['label'] = label

def label_edges(G, labeling_dict):
    for e, label in labeling_dict.items():
        G.edges()[(e[0],e[1])]['label'] = label

def label_edges_with_weights(G):
    '''Label each edge in a graph with its associated weight.'''
    for e in G.edges():
        weight = G.edge[e[0]][e[1]]['weight']
        G.edges[(e[0],e[1])]['label'] = weight

def remove_labels(G, edges=True, nodes=True):
    if nodes:
        for node in G.nodes():
            G.node[node]['label'] = ' '
    if edges:
        for edge in G.edges():
            G.edges()[(edge[0], edge[1])].pop('label', None)

def reset_graph(G):
    color_nodes(G, G.nodes(), 'white')
    color_edges(G, G.edges(), 'black')
    remove_labels(G)
