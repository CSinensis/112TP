from graphClass import *
from backendHelper import *
import copy
"""
References:
TA Mini-Lecture:
https://docs.google.com/presentation/d/1Jcu_qIQDZLIhK71DdDagxv9ayCZgaHVqV5AmNhvXUGU/edit#slide=id.gccceb730df_0_334
Wikipedia:
https://en.wikipedia.org/wiki/Breadth-first_search
Breadth First Search (BFS): Visualized and Explained
https://www.youtube.com/watch?v=xlVX7dXLS64
15122 Notes (thanks Adhvik!):
https://www.cs.cmu.edu/~15122/handouts/24-dfs.pdf
"""
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
#start w/root node in queue and in seen
#loop through nodes in queue (START AT THE FRONT)
#if node is target, return path
#if not, get neighbors of node and append them to the queue

def backtrack(path,start,end):
    actualpath = [end]
    node = end
    while node != start:
        print("FUCKKK")
        for key in path:
            if node in path[key]:
                node = key
                actualpath.append(node)
    return list(reversed(actualpath))
    
def BFS(graph,root,target):
    Q,path = [root],dict()
    graph.seen.add(root)
    if not isConnected(copy.deepcopy(graph),root,target):
        return False, []
    cache = [({root},dict(),root,root,copy.deepcopy(Q))]
    BFSHelper(graph,root,target,Q,path,cache)
    cache = cleanBFSCache(copy.deepcopy(cache),target)
    return backtrack(path,root,target),cache

def BFSHelper(graph,root,target,Q,path,cache):
    node = Q.pop(0)
    if node == target:
        return
    else:
        for i in graph.getNeighbors(node):
            if i not in graph.seen:
                Q.append(i)
                graph.seen.add(i)
                path[node] = path.get(node,set())
                path[node].add(i)
                cache.append((copy.copy(graph.seen),copy.deepcopy(path),node,i,copy.deepcopy(Q)))
        return BFSHelper(graph,root,target,Q,path,cache)

# NON RECURSIVE IN CASE BECAUSE I HATE MYSELF
# def BFS(graph,root,target):
#     seen = set()
#     seen.add(root)
#     Q = [root]
#     path = dict()
#     while len(Q) > 0:
#         print(Q)
#         node = Q.pop(0)
#         if node == target:
#             break
#         for i in graph.getNeighbors(node):
#             if i not in seen:
#                 path[node] = path.get(node,set())
#                 path[node].add(i)
#                 Q.append(i)
#                 seen.add(i)
#     return backtrack(path,root,target)

def main():
    G = Graph(testGraph)
    print(BFS(G,A,F))

if (__name__ == '__main__'):
    main()