testGraph = {
    'A':{'B':2,'C':4},
    'B':{'A':2,'C':3,'D':8},
    'C':{'A':4,'B':3,'E':5,'D':2},
    'D':{'B':8,'C':2,'E':11,'F':22},
    'E':{'C':5,'D':11,'F':1},
    'F':{'D':22,'E':1}
}

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

# Referenced the 15112 mini-lecture slides
# https://docs.google.com/presentation/d/1Jcu_qIQDZLIhK71DdDagxv9ayCZgaHVqV5AmNhvXUGU/edit#slide=id.gccceb730df_0_334
class Graph(object):
    def __init__(self):
        # self.graph = dict()
        self.graph = largerTestGraph
        self.seen = set()
    
    def __repr__(self):
        return f'{self.graph}'

    def addEdge(self,nodeA,nodeB,weight):
        self.graph[nodeA] = self.graph.get(nodeA,dict())
        self.graph[nodeB] = self.graph.get(nodeB,dict())
        self.graph[nodeA][nodeB] = weight
        self.graph[nodeB][nodeA] = weight

    def getEdgeWeight(self,nodeA,nodeB):
        return self.graph[nodeA][nodeB]
    
    def getNodes(self):
        return list(self.graph)
    
    def getNeighbors(self,node):
        return set(self.graph[node])
    
    def orderedNeighbors(self,node):
        L = []
        for neighbor in self.getNeighbors(node):
            L.append((self.getEdgeWeight(node,neighbor),neighbor))
        return sorted(L)