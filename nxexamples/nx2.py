import networkx as nx

g = nx.read_weighted_edgelist('../edgelist.txt')
graphDegree = nx.degree(g)
pos=nx.spring_layout(g)
nx.draw_networkx(g,
        pos,
        node_size=[v * 10 for v in graphDegree.values()],
        with_labels=True,
        font_size=8)

nx.draw_networkx_nodes(g,
                       pos,
                       nodelist=['tirsen',
                       'shen',
                       'mlee',
                       'ged',
                       'objo',
                       'stellsmi',
                       'cowboyd',
                       'asong',
                       'christkv',
                       'hisnice',
                       'duelin_markers',
                       'stillflame'],
                       node_size=300,
                       node_color='g')
