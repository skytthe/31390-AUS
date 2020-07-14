import sys
import numpy as np
import queue

def search_BFS(map, source, target):
    for i in range(len(source)):
        source[i] = int(source[i]-1)
    for i in range(len(target)):
        target[i] = int(target[i]-1)

    map_1d = np.array(map)
    map_3d = np.reshape(map_1d, (10,10,10))

    A = BFS(map_3d, tuple(source), tuple(target))

    # reshape array to fit matlab
    B = np.array(A)
    C = list(B.flat)
    for i in range(len(C)):
        C[i] = C[i]+1
    return C


def BFS(G, source, target):
    q = queue.Queue()
    visited = set()
    parents = {}

    q.put(source)
    visited.add(source)

    step = 1
    while not q.empty():
        #print('step: ', step)
        v = q.get()
        #print('\t active node: ', v)

        if v == target:
            print('BFS')
            print('step: ', step)
            print('\t Goal node')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t cost: ', len(route))
            print('\t route: ', route)
            return route

        n = generateMoves(v, G, 10) # size of map is hard coded

        for i in n:
            if not i in visited:
                q.put(i)
                visited.add(i)
                parents[i] = v

        #print('\t queue: ', q.queue)
        #print('\t visited: ', visited)
        #print('\t parents: ', parents)

        step = step + 1

    return []

def generateMoves(pos, map,size):
    moves = []
    p = list(pos)
    for z in range(3):
        for y in range(3):
            for x in range(3):
                if p[0]+z-1 >= 0 and p[0]+z-1 < size:
                    if p[1]+y-1 >= 0 and p[1]+y-1 < size:
                        if p[2]+x-1 >= 0 and p[2]+x-1 < size:
                            if map[p[2]+x-1,p[1]+y-1,p[0]+z-1] == 0:
                                #print("z ", z-1)
                                #print("y ", y-1)
                                #print("x ", x-1)
                                #print("\n")

                                moves.append(tuple([p[0]+z-1,p[1]+y-1,p[2]+x-1]))

    return moves



def search_Greedy(map, source, target):
    for i in range(len(source)):
        source[i] = int(source[i]-1)
    for i in range(len(target)):
        target[i] = int(target[i]-1)

    map_1d = np.array(map)
    map_3d = np.reshape(map_1d, (10,10,10))

    A = Greedy(map_3d, tuple(source), tuple(target))

    # reshape array to fit matlab
    B = np.array(A)
    C = list(B.flat)
    for i in range(len(C)):
        C[i] = C[i]+1
    return C

def Greedy(G, source, target):
    q = queue.PriorityQueue()
    visited = set()
    parents = {}

    q.put((calcHeuristic(source, target), source))
    visited.add(source)

    step = 1
    while not q.empty():
        #print('step: ', step)
        v = q.get()[1]
        #print('\t active node: ', v)

        if v == target:
            print('Greedy')
            print('step: ', step)
            print('\t Goal node')
            route = [target]
            while not route[-1] == source:
                route.append(parents[route[-1]])
            route.reverse()
            print('\t cost: ', len(route))
            print('\t route: ', route)
            return route

        n = generateMoves(v, G, 10) # size of map is hard coded

        for i in n:
            if not i in visited:
                q.put((calcHeuristic(i, target), i))
                visited.add(i)
                parents[i] = v

        #print('\t queue: ', q.queue)
        #print('\t visited: ', visited)
        #print('\t parents: ', parents)

        step = step + 1

    return []

def calcHeuristic(pos, target):
    return np.sqrt( np.power((pos[0]-target[0]),2) + np.power((pos[1]-target[1]),2) + np.power((pos[2]-target[2]),2))


def search_Astar(map, source, target):
    for i in range(len(source)):
        source[i] = int(source[i]-1)
    for i in range(len(target)):
        target[i] = int(target[i]-1)

    map_1d = np.array(map)
    map_3d = np.reshape(map_1d, (10,10,10))

    A = Astar(map_3d, tuple(source), tuple(target))

    # reshape array to fit matlab
    B = np.array(A)
    C = list(B.flat)
    for i in range(len(C)):
        C[i] = C[i]+1
    return C

def Astar(G, source, target):
    cost = {}
    visited = {}
    discovered = set()

    cost[source] = (calcHeuristic(source, target), 0, source) # (cost+heuristic, cost, parent) 
    discovered.add(source)

    step = 1
    while bool(cost):
        #print('step: ', step)
        v = min(cost, key=cost.get)
        visited[v] = cost.pop(v)
        #print('\t active node: ', v)

        if v == target:
            print('Astar')
            print('step: ', step)
            print('\t Goal node')
            #print('\t cost: ', visited[v][1])
            route = [target]
            while not route[-1] == source:
                route.append(visited[route[-1]][2])
            route.reverse()
            print('\t cost: ', len(route))
            print('\t route: ', route)
            return route

        n = generateMoves(v, G, 10) # size of map is hard coded

        for i in n:
            if not i in visited and not i in discovered:
                cost[i] = ( 1 + visited[v][1] + calcHeuristic(i, target),
                            1 + visited[v][1],
                            v)
                discovered.add(i)
            if not i in visited and i in discovered:
                if(cost[i][1] > 1 + visited[v][1]):
                    cost[i] = ( 1 + visited[v][1] + calcHeuristic(i, target),
                                1 + visited[v][1],
                                v)
        #print('\t cost: ', cost)
        #print('\t visited: ', visited)
        #print('\t discovered: ', discovered)

        step = step + 1

    return []
