from graphClass import *
from queue import PriorityQueue
from backendHelper import *
import copy
# FILE FUNCTION: Contains A* algorithm
"""
References:
TA Mini-Lecture:
https://docs.google.com/presentation/d/1Jcu_qIQDZLIhK71DdDagxv9ayCZgaHVqV5AmNhvXUGU/edit#slide=id.gccceb730df_0_334
Wikipedia:
https://en.wikipedia.org/wiki/A*_search_algorithm
A* Pathfinding (E01: algorithm explanation):
https://www.youtube.com/watch?v=-L-WgKMFuhE
Graph Data Structure 6. The A* Pathfinding Algorithm:
https://www.youtube.com/watch?v=eSOJ3ARN5FM
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

def backtrack(costs,root,target):
    print(costs)
    path = [target,f'Total Cost: {costs[target][2]}']
    node = target
    while node != root:
        node = costs[node][3]
        path.insert(0,node)
    return path

def aStar(G,root,target):
    Q = PriorityQueue()
    initialHCost = h(root,target)
    Q.put((initialHCost,initialHCost,0,root))
    costs = setCosts(G,root)
    if not isConnected(copy.deepcopy(G),root,target):
        return False, []
    cache = [({root},copy.deepcopy(costs),root,root,copy.deepcopy(sorted(Q.queue)))]
    aStarHelper(G,target,Q,costs,cache)
    cache = cleanCache(copy.deepcopy(cache),target)
    return backtrack(costs,root,target),cache

def aStarHelper(G,target,Q,costs,cache):
    if target in G.seen:
        cache.append((copy.copy(G.seen),copy.deepcopy(costs),target,target,copy.deepcopy(sorted(Q.queue))))
        return
    else:
        (TCost,HCost,GCost,node) = Q.get()
        G.seen.add(node)
        for neighbor in G.getNeighbors(node):
            if neighbor not in G.seen:
                newGCost = GCost + G.getEdgeWeight(node,neighbor)
                newHCost = h(neighbor,target)
                newTCost = newGCost + newHCost
                if newTCost < costs[neighbor][0]:
                    if costs[neighbor][0] != float('inf'):
                        Q.queue.remove((costs[neighbor][0],costs[neighbor][1],costs[neighbor][2],neighbor))
                    Q.put((newTCost,newHCost,newGCost,neighbor))
                    costs[neighbor] = (newTCost,newHCost,newGCost,node)
                cache.append((copy.copy(G.seen),copy.deepcopy(costs),node,neighbor,copy.deepcopy(sorted(Q.queue))))
        aStarHelper(G,target,Q,costs,cache)
