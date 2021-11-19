from graphClass import *
from queue import PriorityQueue
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
testCoords2 = {'X':(20,10),'A':(0,10),'B':(10,10),
'C':(30,10),'D':(0,20),'E':(40,0),'F':(0,30),'G':(10,30),
'H':(10,20),'I':(30,30),'J':(40,30),'K':(30,40),'L':(30,20),'Y':(20,50),
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
    return (abs(testCoords[node][0] - testCoords[target][0])
    + abs(testCoords[node][1] - testCoords[target][1]))

def backtrack(costs,root,target):
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
    aStarHelper(G,target,Q,costs)
    print(G.seen)
    return backtrack(costs,root,target)

def aStarHelper(G,target,Q,costs):
    if target in G.seen:
        return
    else:
        (TCost,HCost,GCost,node) = Q.get()
        G.seen.add(node)
        print(TCost,node)
        for neighbor in G.getNeighbors(node):
            if neighbor not in G.seen:
                newGCost = GCost + G.getEdgeWeight(node,neighbor)
                newHCost = h(neighbor,target)
                newTCost = newGCost + newHCost
                if newTCost < costs[neighbor][0]:
                    Q.put((newTCost,newHCost,newGCost,neighbor))
                    costs[neighbor] = (newTCost,newHCost,newGCost,node)
        aStarHelper(G,target,Q,costs)

def main():
    G = Graph()
    print(aStar(G,'L','A'))

if (__name__ == '__main__'):
    main()