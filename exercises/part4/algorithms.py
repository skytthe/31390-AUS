#!/usr/bin/env python3

import networkx as nx
import queue
import pprint

def BFS(G, source, target):
    q = queue.Queue()
    visited = set()
    parents = {}

    q.put(source)
    visited.add(source)

    step = 1
    while not q.empty():
        print('step: ', step)
        v = q.get()
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t route: ', route)
            return route

        n = list(G.adj[v])

        for i in n:
            if not i in visited:
                q.put(i)
                visited.add(i)
                parents[i] = v

        print('\t queue: ', q.queue)
        print('\t visited: ', visited)
        print('\t parents: ', parents)

        step = step + 1

    return []


def DFS_low(G, source, target):
    q = queue.LifoQueue()
    visited = set()
    parents = {}

    q.put(source)
    visited.add(source)

    step = 1
    while not q.empty():
        print('step: ', step)
        v = q.get()
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t route: ', route)
            return route

        n = sorted(list(G.adj[v]), reverse=True)

        for i in n:
            if not i in visited:
                q.put(i)
                visited.add(i)
                parents[i] = v

        print('\t queue: ', q.queue)
        print('\t visited: ', visited)
        print('\t parents: ', parents)

        step = step + 1

    return []


def DFS_low_CHRISTOPHER(G, source, target):
    q = queue.LifoQueue()
    visited = set()
    parents = {}

    q.put(source)

    step = 1
    while not q.empty():
        print('step: ', step)
        v = q.get()
        visited.add(v)
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t route: ', route)
            return route

        n = sorted(list(G.adj[v]), reverse=True)

        for i in n:
            if not i in visited:
                q.put(i)
                parents[i] = v

        print('\t queue: ', q.queue)
        print('\t visited: ', visited)
        print('\t parents: ', parents)

        step = step + 1

    return []


def DFS_high(G, source, target):
    q = queue.LifoQueue()
    visited = set()
    parents = {}

    q.put(source)
    visited.add(source)

    step = 1
    while not q.empty():
        print('step: ', step)
        v = q.get()
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t route: ', route)
            return route

        n = sorted(list(G.adj[v]), reverse=False)

        for i in n:
            if not i in visited:
                q.put(i)
                visited.add(i)
                parents[i] = v

        print('\t queue: ', q.queue)
        print('\t visited: ', visited)
        print('\t parents: ', parents)

        step = step + 1

    return []

def DFS_high_CHRISTOPHER(G, source, target):
    q = queue.LifoQueue()
    visited = set()
    parents = {}

    q.put(source)

    step = 1
    while not q.empty():
        print('step: ', step)
        v = q.get()
        visited.add(v)
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t route: ', route)
            return route

        n = sorted(list(G.adj[v]), reverse=False)

        for i in n:
            if not i in visited:
                q.put(i)
                parents[i] = v

        print('\t queue: ', q.queue)
        print('\t visited: ', visited)
        print('\t parents: ', parents)

        step = step + 1

    return []



def Dijkstra(G, source, target):
    cost = {}
    visited = {}
    discovered = set()

    cost[source] = (0,source) # (cost, parent) 
    discovered.add(source)

    step = 1
    while bool(cost):
        print('step: ', step)
        v = min(cost, key=cost.get)
        visited[v] = cost.pop(v)
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            print('\t cost: ', visited[v][0])
            route = [target]
            while not route[-1] == source:
                route.append(visited[route[-1]][1])
            route.reverse()
            print('\t route: ', route)
            return route

        n = G.adj[v]

        for i in n:
            if not i in visited and not i in discovered:
                cost[i] = (G[v][i]['weight'] + visited[v][0]
                            ,v)
                discovered.add(i)
            if not i in visited and i in discovered:
                if(cost[i][0] > G[v][i]['weight'] + visited[v][0]):
                    cost[i] = (G[v][i]['weight'] + visited[v][0]
                                ,v)
        print('\t cost: ', cost)
        print('\t visited: ', visited)
        print('\t discovered: ', discovered)

        step = step + 1

    return []


def Greedy(G, source, target):
    q = queue.PriorityQueue()
    visited = set()
    parents = {}

    q.put((G.nodes[source]['heuristic'], source))
    visited.add(source)

    step = 1
    while not q.empty():
        print('step: ', step)
        v = q.get()[1]
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t route: ', route)
            return route

        n = G.adj[v]

        for i in n:
            if not i in visited:
                q.put((G.nodes[i]['heuristic'], i))
                visited.add(i)
                parents[i] = v

        print('\t queue: ', q.queue)
        print('\t visited: ', visited)
        print('\t parents: ', parents)

        step = step + 1

    return []


def Astar(G, source, target):
    cost = {}
    visited = {}
    discovered = set()

    cost[source] = (G.nodes[source]['heuristic'], 0, source) # (cost+heuristic, cost, parent) 
    discovered.add(source)

    step = 1
    while bool(cost):
        print('step: ', step)
        v = min(cost, key=cost.get)
        visited[v] = cost.pop(v)
        print('\t active node: ', v)

        if v == target:
            print('\t Goal node found')
            print('\t cost: ', visited[v][1])
            route = [target]
            while not route[-1] == source:
                route.append(visited[route[-1]][2])
            route.reverse()
            print('\t route: ', route)
            return route

        n = G.adj[v]

        for i in n:
            if not i in visited and not i in discovered:
                cost[i] = ( G[v][i]['weight'] + visited[v][1] + G.nodes[i]['heuristic'],
                            G[v][i]['weight'] + visited[v][1],
                            v)
                discovered.add(i)
            if not i in visited and i in discovered:
                if(cost[i][1] > G[v][i]['weight'] + visited[v][1]):
                    cost[i] = ( G[v][i]['weight'] + visited[v][1] + G.nodes[i]['heuristic'],
                                G[v][i]['weight'] + visited[v][1],
                                v)
        print('\t cost: ', cost)
        print('\t visited: ', visited)
        print('\t discovered: ', discovered)

        step = step + 1

    return []

    