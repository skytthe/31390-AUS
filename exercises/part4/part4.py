#!/usr/bin/env python3

import numpy as np
import networkx as nx

from graph import createGraph
from algorithms import *


if __name__ == "__main__":

    G = createGraph()

    print('###############')
    print('# DFS_low #####')
    print('###############')
    DFS_low(G,0,23)
    print('\n\n')

    print('###################')
    print('# DFS_christopher #')
    print('###################')
    DFS_low_CHRISTOPHER(G,0,23)
    print('\n\n')

    print('###############')
    print('# DFS_high    #')
    print('###############')
    DFS_high(G,0,23)
    print('\n\n')

    print('###############')
    print('# BFS         #')
    print('###############')
    BFS(G,0,23)
    print('\n\n')

    print('####################')
    print('# Dijkstra         #')
    print('####################')
    Dijkstra(G,0,23)
    print('\nnx implementation results:')
    print('\t', nx.dijkstra_path(G,0,23))
    print('\t', nx.dijkstra_path_length(G,0,23))
    print('\n\n')

    print('####################')
    print('# Greedy           #')
    print('####################')
    Greedy(G,0,23)
    print('\n\n')

    print('####################')
    print('# Astar            #')
    print('####################')
    Astar(G,0,5)
    print('\n')
    print('\nnx implementation results:')
    print('\t', nx.dijkstra_path(G,0,23))
    print('\t', nx.dijkstra_path_length(G,0,23))
    print('\n\n')

    exit()
