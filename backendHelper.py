from graphClass import *

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
