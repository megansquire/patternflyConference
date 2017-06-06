import networkx as nx

g = nx.read_weighted_edgelist('../edgelist2.txt')

graphs = list(nx.connected_component_subgraphs(g))
for graph in graphs:
    if graph.has_node('tirsen'):
        ego = nx.Graph(nx.ego_graph(graph, 'tirsen', radius=1))
        graphDegree = nx.degree(ego)

        pos=nx.spring_layout(ego)

        nx.draw(ego,
            pos,
            node_size=[v * 10 for v in graphDegree.values()],
            with_labels=True,
            font_size=8)
        
        nx.draw_networkx_nodes(ego, 
                               pos, 
                               nodelist=['tirsen'],
                               node_size=300, 
                               node_color='g')
                               
