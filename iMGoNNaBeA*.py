from graphClass import *
from queue import PriorityQueue
largerTestGraph = {
    'X':{'E':4,'A':7,'B':2,'C':3},
    'A':{'X':7,'B':3,'D':4},
    'B':{'X':2,'A':3,'D':4,'H':5},
    'C':{'X':3,'L':2},
    'D':{'A':4,'B':4,'F':1},
    'E':{'X':4},
    'F':{'D':1,'H':3},
    'G':{'H':2,'Y':2},
    'H':{'G':2,'B':5,'F':3},
    'I':{'L':4,'J':6,'K':4},
    'J':{'L':1,'I':6},
    'K':{'I':4,'Y':5},
    'L':{'C':2,'I':4,'J':1},
    'Y':{'G':2,'K':5},
}
# tuples in form X,Y
testCoords = {'X':(2,1),'A':(0,1),'B':(1,1),
'C':(3,1),'D':(0,2),'E':(4,0),'F':(0,3),'G':(1,3),
'H':(1,2),'I':(3,3),'J':(4,3),'K':(3,4),'L':(3,2),'Y':(2,5),
}

def setCosts(G,root):
    cost = dict()
    for key in G.graph:
        if key == root:
            cost[key] = (0,)
        else:
            #help
            cost[key] = (10000000000000000000,)
    return cost

def h(node,target):
    return ((testCoords[node][0] - testCoords[target][0])
    + (testCoords[node][1] - testCoords[target][1]))

def g(node,root):
    return 
    return

def getSortedDict(cost):
    return dict(sorted(cost.items(),key=lambda cost: cost[1]))

def backtrack(costs,root,target):
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
    return backtrack(costs,root,target)

def dijkHelper(G,target,Q,costs):
    if target in G.seen:
        return
    else:
        (cost,node) = Q.get()
        G.seen.add(node)
        for neighbor in G.getNeighbors(node):
            if neighbor not in G.seen:
                newCost = cost + G.getEdgeWeight(node,neighbor)
                if newCost < costs[neighbor][0]:
                    Q.put((newCost,neighbor))
                    costs[neighbor] = (newCost,node)
        dijkHelper(G,target,Q,costs)