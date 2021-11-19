from graphClass import *
#can i even use this?
from queue import PriorityQueue

"""
Sources:
Dijkstra's Algorithm - Computerphile: 
https://www.youtube.com/watch?v=GazC3A4OQTE
Graph Data Structure 4. Dijkstra’s Shortest Path Algorithm: 
https://www.youtube.com/watch?v=pVfj6mxhdMw
Priority Queue:
https://www.educative.io/edpresso/what-is-the-python-priority-queue
Wikipedia:

"""

def setCosts(G,root):
    cost = dict()
    for key in G.graph:
        if key == root:
            cost[key] = (0,)
        else:
            #help
            cost[key] = (10000000000000000000,)
    return cost

# def getSortedDict(cost):
#     return dict(sorted(cost.items(),key=lambda cost: cost[1]))

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
    dijkHelper(G,target,Q,costs)
    print(G.seen)
    return backtrackDijkstra(costs,root,target)

def dijkHelper(G,target,Q,costs):
    if target in G.seen:
        return
    else:
        (cost,node) = Q.get()
        G.seen.add(node)
        print(node)
        for neighbor in G.getNeighbors(node):
            if neighbor not in G.seen:
                newCost = cost + G.getEdgeWeight(node,neighbor)
                if newCost < costs[neighbor][0]:
                    Q.put((newCost,neighbor))
                    costs[neighbor] = (newCost,node)
        dijkHelper(G,target,Q,costs)

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
        
def main():
    G = Graph()
    print(dijkstra(G,'L','A'))

if (__name__ == '__main__'):
    main()