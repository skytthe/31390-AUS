#!/usr/bin/env python3

import networkx as nx

def createGraph():
    G = nx.Graph()

    nodeHeuristics = [  17.0,
                        15.5,
                        11.0,
                        15.1,
                        13.4,
                        10.8,
                        10.2,
                        12.4,
                        15.2,
                        8.6,
                        6.7,
                        11.7,
                        5.1,
                        7.3,
                        6.7,
                        6.7,
                        4.5,
                        3.2,
                        5.1,
                        2.8,
                        7.1,
                        2.0,
                        3.2,
                        0.0
                        ]

    for n in range(len(nodeHeuristics)):
        G.add_node(n, heuristic = nodeHeuristics[n])

    # from node 0
    G.add_edges_from([(0, 1, {'weight': 4.5}), (0, 2, {'weight': 5.4}), (0, 3, {'weight': 2.2})])
    # from node 1
    G.add_edges_from([(1, 2, {'weight': 4.2}), (1, 4, {'weight': 2.2})])
    # from node 2
    G.add_edges_from([(2, 5, {'weight': 3.6}), (2, 6, {'weight': 3.2})])
    # from node 3
    G.add_edges_from([(3, 7, {'weight': 2.2}), (3, 8, {'weight': 3.2})])
    # from node 4
    G.add_edges_from([(4, 5, {'weight': 1.4})])
    # from node 5
    G.add_edges_from([(5, 9, {'weight': 2.2})])
    # from node 6
    G.add_edges_from([(6, 7, {'weight': 1.4}), (6, 10, {'weight': 2.0})])
    # from node 7
    G.add_edges_from([(7, 8, {'weight': 2.2}), (7, 11, {'weight': 2.2})])
    # from node 8
    G.add_edges_from([(8, 11, {'weight': 3.2})])
    # from node 9
    G.add_edges_from([(9, 12, {'weight': 6.0}), (9, 13, {'weight': 3.0})])
    # from node 10
    G.add_edges_from([(10, 13, {'weight': 4.0})])
    # from node 11
    G.add_edges_from([(11, 14, {'weight': 4.1}), (11, 15, {'weight': 6.0})])
    # from node 12
    G.add_edges_from([(12, 16, {'weight': 3.2}), (12, 17, {'weight': 3.6}), (12, 23, {'weight': 5.1})])
    # from node 13
    G.add_edges_from([(13, 18, {'weight': 3.2})])
    # from node 14
    G.add_edges_from([(14, 15, {'weight': 1.4}), (14, 18, {'weight': 2.0})])
    # from node 15
    G.add_edges_from([(15, 19, {'weight': 3.2}), (15, 20, {'weight': 2.2})])
    # from node 16
    G.add_edges_from([(16, 21, {'weight': 4.0})])
    # from node 17
    G.add_edges_from([(17, 18, {'weight': 3.6}), (17, 19, {'weight': 4.1}), (17, 23, {'weight': 3.2})])
    # from node 18
    #   none
    # from node 19
    G.add_edges_from([(19, 20, {'weight': 4.5}), (19, 23, {'weight': 2.8})])
    # from node 20
    G.add_edges_from([(20, 22, {'weight': 3.6})])
    # from node 21
    G.add_edges_from([(21, 22, {'weight': 3.6}), (21, 23, {'weight': 2.0})])
    # from node 22
    G.add_edges_from([(22, 23, {'weight': 3.2})])
    # from node 23
    #   none

    return G
