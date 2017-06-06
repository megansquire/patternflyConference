#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_weighted_edgelist('edgelist.txt')
degree = nx.degree(g)

# then, pull out each of these connected components
# and sort them by the number of nodes in them
graphs = list(nx.connected_component_subgraphs(g))
graphsSorted = sorted(graphs, key=len, reverse=True)

# for the top five largest graphs, print the number of nodes
# and save the graph to a file
i = 0
for graph in graphsSorted[0:5]:
    i += 1
    graphDegree = nx.degree(graph)

    f1 = plt.figure()
    nx.draw_networkx(graph,
                     node_size=[v * 10 for v in graphDegree.values()],
                     with_labels=True,
                     font_size=8)
    filename1 = 'graphLabels' + str(i) + '.png'
    f1.savefig(filename1)
