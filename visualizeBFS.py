from cmu_112_graphics import *
from graphClass import *
from BFS import *
from visualizeHelper import *

# A = Node(4,2,'A')
# B = Node(3,4,'B')
# C = Node(5,4,'C')
# D = Node(7,4,'D')
# E = Node(4,6,'E')
# F = Node(6,6,'F')
# G = Node(7,8,'G')
# H = Node(3,7,'H')
# # testGraph = {
# #     A:{B:2,C:4,D:3},
# #     B:{A:2},
# #     C:{A:4,E:5,F:2},
# #     D:{A:3,F:8},
# #     E:{C:5,H:6},
# #     F:{D:8,C:5,G:3},
# #     G:{F:3},
# #     H:{E:6}
# # }
# testGraph = {
#     A:{B:2,C:4,D:3},
#     B:{A:2},
#     C:{A:4,E:5,F:2},
#     D:{A:3,F:8},
#     E:{C:5},
#     F:{D:8,C:5}
# }

def BFS_mousePressed(app,event):
    if inForBounds(app,event.x,event.y) and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif inBackBounds(app,event.x,event.y) and app.step > 0:
        app.step -= 1
        applyState(app)
    elif inCustomBounds(app,event.x,event.y):
        app.mode = 'create'
        resetCustom(app)
    else:
        toggleOptions(app,event.x,event.y)

def BFS_keyPressed(app,event):
    if event.key == 'Right' and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif event.key == 'Left' and app.step > 0:
        app.step -= 1
        applyState(app)
    elif event.key == 't':
        app.mode = 'dijk'
        app.cache = None
        reset(app)
        print(app.cache)
    elif event.key == 'r':
        reset(app)
    elif event.key == 'n':
        print("HERE")
        app.gMode = 'HC2'
        reset(app)

def applyState(app):
    if app.cache == None:
        blah,app.cache = BFS(app.G,app.startNode,app.endNode)
    if app.step < len(app.cache):
        state = app.cache[app.step]
        seen,path,current,Q = state
        edges = pathToEdges(app,path,current)
        app.Q = Q
        for node in app.nodes:
            if node == current:
                node.color = myGreen
            elif node in seen:
                node.color = 'grey'
            else:
                node.color = 'red'
        for edge in app.edges:
            if edge.path in edges:
                edge.color = myGreen
            else:
                edge.color = 'black'

def BFS_timerFired(app):
    if app.auto and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.cache != None and app.step < len(app.cache):
        app.auto = False

def pathToEdges(app,path,current):
    edges = set()
    node = current
    while node != app.startNode:
        for key in path:
            if node in path[key]:
                edges.add((key,node))
                node = key
    return edges

def drawEdges(app,canvas):
    for edge in app.edges:
        n1,n2 = edge.path
        x1,y1 = gridToCoord(app,n1.x,n1.y)
        x2,y2 = gridToCoord(app,n2.x,n2.y)
        avgX,avgY = (x1+x2)/2,(y1+y2)/2
        canvas.create_line(x1,y1,x2,y2,fill=edge.color)

def drawNodes(app,canvas):
    for node in app.nodes:
        cx,cy = gridToCoord(app,node.x,node.y)
        r = node.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=node.color)
        canvas.create_text(cx,cy,text=f'{node.label}')

def BFS_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)

