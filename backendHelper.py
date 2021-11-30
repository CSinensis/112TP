from graphClass import *

A = Node(4,2,'A')
B = Node(3,4,'B')
C = Node(5,4,'C')
D = Node(7,4,'D')
E = Node(4,6,'E')
F = Node(6,6,'F')
testGraph1 = {
    A:{B:2},
    B:{A:2},
    C:{E:5},
    E:{C:5},
}

A = Node(4,2,'A')
B = Node(3,4,'B')
C = Node(5,4,'C')
D = Node(7,4,'D')
E = Node(4,6,'E')
F = Node(6,6,'F')
testGraph2 = {
    A:{B:2,C:4,D:3},
    B:{A:2},
    C:{A:4,E:5,F:2},
    D:{A:3,F:8},
    E:{C:5},
    F:{D:8,C:5}
}

X = Node(5,1,'X')
A = Node(2,3,'A')
B = Node(4,3,'B')
C = Node(7,3,'C')
D = Node(2,5,'D')
E = Node(8,1,'E')
F = Node(2,7,'F')
G = Node(4,7,'G')
H = Node(4,5,'H')
I = Node(7,6,'I')
J = Node(9,6,'J')
K = Node(6,8,'K')
L = Node(8,4,'L')
Y = Node(5,9,'Y')
largerTestGraph = {
X:{E:4,A:7,B:3,C:5},
A:{X:7,B:3,D:4},
B:{X:3,A:3,D:4,H:2},
C:{X:5,L:2},
D:{A:4,B:4,F:2},
E:{X:4},
F:{D:2,H:5},
G:{H:2,Y:4},
H:{G:2,B:2,F:5},
I:{L:4,J:6,K:4},
J:{L:7,I:6},
K:{I:4,Y:5},
L:{C:2,I:4,J:7},
Y:{G:4,K:5}}

def isConnected(G,root,target):
    Q = [root]
    result = connectHelper(G,root,target,Q)
    return result

def connectHelper(graph,root,target,Q):
    if len(Q) == 0:
        return False
    node = Q.pop(0)
    if node == target:
        return True
    else:
        for i in graph.getNeighbors(node):
            if i not in graph.seen:
                Q.append(i)
                graph.seen.add(i)
        return connectHelper(graph,root,target,Q)

def cleanCache(cache,target):
    for i in range(len(cache)):
        if cache[i][2] == target:
            seen,cost,current,check,Q = cache[i]
            return cache[:i] + [(seen,cost,current,check,[])]

def cleanBFSCache(cache,target):
    for i in range(len(cache)):
        if cache[i][3] == target:
            seen,path,current,check,Q = cache[i]
            return cache[:i] + [cache[i],(seen,path,target,check,[])]

def h(node,target):
    return (abs(node.x-target.x) + abs(node.y-target.y))

def main():
    G = Graph(largerTestGraph)
    print(isConnected(G,X,Y))

if (__name__ == '__main__'):
    main()