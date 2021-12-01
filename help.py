# from cmu_112_graphics import *
# from visualizeHelper import *

# def help_mousePressed(app,event):
#     return

# def help_timerFired(app):
#     return

# def drawBackground(app,canvas):
#     canvas.create_rectangle(app.screenMargin,app.screenMargin,
#     app.width-app.screenMargin,app.height-app.screenMargin,fill=myBlue)

# def help_redrawAll(app,canvas):
#     drawBackground(app,canvas)
#     return

# def help_appStarted(app):
#     return

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

#NON RECURSIVE IMPLEMENTATION IN CASE:

# def dij(G,root,target):
#     Q = PriorityQueue()
#     Q.put((0,root))
#     costs = setCosts(G,root)
#     while not Q.empty():
#         (cost,node) = Q.get()
#         G.seen.add(node)
#         for neighbor in G.getNeighbors(node):
#             if neighbor not in G.seen:
#                 newCost = cost + G.getEdgeWeight(node,neighbor)
#                 if newCost < costs[neighbor][0]:
#                     Q.put((newCost,neighbor))
#                     costs[neighbor] = (newCost,node)
#     path = backtrackDijkstra(costs,root,target)
#     return path