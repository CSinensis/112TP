from graphClass import *
from queue import PriorityQueue
import copy
"""
References:
TA Mini-Lecture:
https://docs.google.com/presentation/d/1Jcu_qIQDZLIhK71DdDagxv9ayCZgaHVqV5AmNhvXUGU/edit#slide=id.gccceb730df_0_334
Dijkstra's Algorithm - Computerphile: 
https://www.youtube.com/watch?v=GazC3A4OQTE
Graph Data Structure 4. Dijkstra’s Shortest Path Algorithm: 
https://www.youtube.com/watch?v=pVfj6mxhdMw
Priority Queue:
https://www.educative.io/edpresso/what-is-the-python-priority-queue
Wikipedia:
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

def setCosts(G,root):
    cost = dict()
    inf = float('inf')
    for key in G.graph:
        if key == root:
            cost[key] = (0,)
        else:
            cost[key] = (inf,)
    return cost

def backtrackDijkstra(costs,root,target): 
    path = [target,f'Total Cost: {costs[target][0]}']
    node = target
    while node != root:
        node = costs[node][1]
        path.insert(0,node)
    return path

def dijkstra(G,root,target):
    Q = PriorityQueue()
    Q.put((0,root))
    costs = setCosts(G,root)
    path = dict()
    cache = [({root},copy.deepcopy(costs),root,root,[])]
    dijkHelper(G,target,Q,costs,path,cache)
    return backtrackDijkstra(costs,root,target),cache

def dijkHelper(G,target,Q,costs,path,cache):
    if target in G.seen:
        return
    else:
        (cost,node) = Q.get()
        G.seen.add(node)
        for neighbor in G.getNeighbors(node):
            cache.append((copy.copy(G.seen),copy.deepcopy(costs),node,neighbor,copy.deepcopy(sorted(Q.queue))))
            if neighbor not in G.seen:
                newCost = cost + G.getEdgeWeight(node,neighbor)
                if newCost < costs[neighbor][0]:
                    if costs[neighbor][0] != float('inf'):
                        Q.queue.remove((costs[neighbor][0],neighbor))
                    Q.put((newCost,neighbor))
                    costs[neighbor] = (newCost,node)
                path[node] = path.get(node,set())
                path[node].add(neighbor)
        dijkHelper(G,target,Q,costs,path,cache)

#NON RECURSIVE IMPLEMENTATION IN CASE:

# def dij(G,root,target):
#     Q = PriorityQueue()
#     Q.put((0,root))
#     costs = setCosts(G,root)
#     while not Q.empty():
#         (cost,node) = Q.get()
#         G.seen.add(node)
#         for neighbor in G.getNeighbors(node):
#             if neighbor not in G.seen:
#                 newCost = cost + G.getEdgeWeight(node,neighbor)
#                 if newCost < costs[neighbor][0]:
#                     Q.put((newCost,neighbor))
#                     costs[neighbor] = (newCost,node)
#     path = backtrackDijkstra(costs,root,target)
#     return path

A = Node(4,2,'A')
B = Node(3,4,'B')
C = Node(5,4,'C')
D = Node(7,4,'D')
E = Node(4,6,'E')
F = Node(6,6,'F')

testGraph = {
    A:{B:2,C:4,D:3},
    B:{A:2},
    C:{A:4,E:5,F:2},
    D:{A:3,F:8},
    E:{C:5},
    F:{D:8,C:5}
}

def main():
    G = Graph(testGraph)
    print(dijkstra(G,A,F))

if (__name__ == '__main__'):
    main()