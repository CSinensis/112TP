from graphClass import *

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
#start w/root node in queue and in seen
#loop through nodes in queue (START AT THE FRONT)
#if node is target, return path
#if not, get neighbors of node and append them to the queue

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
    return BFSHelper(graph,root,target,Q,path)

def BFSHelper(graph,root,target,Q,path):
    node = Q.pop(0)
    if node == target:
        return backtrack(path,root,target)
    else:
        for i in graph.getNeighbors(node):
            if i not in graph.seen:
                Q.append(i)
                graph.seen.add(i)
                path[node] = path.get(node,set())
                path[node].add(i)
        return BFSHelper(graph,root,target,Q,path)

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
    G = Graph()
    print(BFS(G,'X','Y'))

if (__name__ == '__main__'):
    main()