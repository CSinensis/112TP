from graphClass import *
from backendHelper import *
import copy
# FILE FUNCTION: Contains BFS Algorithm
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

def backtrack(path,start,end):
    actualpath = [end]
    node = end
    while node != start:
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

