#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx

g = nx.read_weighted_edgelist('edgelist.txt')
degree = nx.degree(g)

# (1) remove nodes that only have one connection, to shrink size of drawing
g2 = g.copy()
d2 = nx.degree(g2)
for n in g2.nodes():
    if d2[n] <= 2:
        g2.remove_node(n)

# (2) scale the size of the node to its degree (high-degree nodes are bigger)
nx.draw_networkx(g2,
                 node_size=[v * 10 for v in d2.values()],
                 with_labels=False)
