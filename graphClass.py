# FILE FUNCTION: Contains all classes used throughout project (Graph,Edges,Nodes etc...)
# Referenced the 15112 mini-lecture slides
# https://docs.google.com/presentation/d/1Jcu_qIQDZLIhK71DdDagxv9ayCZgaHVqV5AmNhvXUGU/edit#slide=id.gccceb730df_0_334
class Graph(object):
    def __init__(self,graph):
        self.graph = graph
        self.seen = set()
        self.start = None
        self.end = None
        self.img = None
        self.imgMode = False
        self.url = None
    
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

class Node(object):
    def __init__(self,x,y,label):
        self.x = x
        self.y = y
        self.r = 10
        self.label = label
        self.color = 'red3'

    def __repr__(self):
        return f'{self.label}'
    
    def __eq__(self,other):
        return isinstance(other,Node) and self.label == other.label
    
    def __lt__(self,other):
        return self.label < other.label

    def getHashables(self):
        return (self.x,self.y,self.r,self.label)
    
    def __hash__(self):
        return hash(self.getHashables())

class Edge(object):
    def __init__(self,start,end):
        self.path = (start,end)
        self.color = 'black'
        self.weight = 1

    def __eq__(self,other):
        return isinstance(other,Edge) and set(self.path) == set(other.path)
    
    def __repr__(self):
        return f'{self.path}'

    def getHashables(self):
        return (self.path)

    def __hash__(self):
        return hash(self.getHashables)

class Cell(object):
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.role = 'black'
        self.walls = [True,True,True,True]
    
    def __repr__(self):
        return f'{self.row},{self.col},{self.role}'

    def draw(self,app,canvas):
        x = app.startX + self.col*app.s
        y = app.startY+self.row*app.s
        canvas.create_rectangle(x,y,x+app.s,y+app.s,fill=self.role,width=0)
        