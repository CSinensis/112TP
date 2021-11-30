from cmu_112_graphics import *
from graphClass import *
from BFS import *
from visualizeHelper import *
# import pygame
# from pygame.locals import *
# from pygame import mixer

def BFS_mousePressed(app,event):
    if inCustomBounds(app,event.x,event.y):
        app.mode = 'create'
        resetCustom(app)
    elif inResetBounds(app,event.x,event.y):
        reset(app)
    elif app.G.graph != dict() and inForBounds(app,event.x,event.y) and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.G.graph != dict() and inBackBounds(app,event.x,event.y) and app.step > 0:
        app.step -= 1
        applyState(app)
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

# def applyState(app):
#     if app.cache == None:
#         print(app.G.start,app.G.end)
#         blah,app.cache = BFS(app.G,app.G.start,app.G.end)
#         print(app.cache)
#     if app.step < len(app.cache):
#         state = app.cache[app.step]
#         seen,path,current,Q = state
#         edges = pathToEdges(app,path,current)
#         app.Q = Q[:6]
#         for node in app.nodes:
#             if node == current:
#                 node.color = myGreen
#             elif node in seen:
#                 node.color = 'grey'
#             else:
#                 node.color = 'red'
#         for edge in app.edges:
#             if edge.path in edges:
#                 edge.color = myGreen
#             else:
#                 edge.color = 'black'

def applyState(app):
    if app.cache == None:
        print(app.G,app.G.start,app.G.end)
        app.solution,app.cache = BFS(app.G,app.G.start,app.G.end)
    if app.step < len(app.cache):
        state = app.cache[app.step]
        print(state)
        seen,path,current,check,Q = state
        edges = pathToEdges(app,path,current)
        app.Q = Q[:6]
        for node in app.nodes:
            if node == current:
                node.color = myGreen
            elif node == check and current != app.G.end:
                node.color = myBlue
            elif node in seen:
                node.color = 'grey'
            else:
                node.color = 'red3'
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
    while node != app.G.start:
        for key in path:
            if node in path[key]:
                edges.add((key,node))
                edges.add((node,key))
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

def drawQueueText(app,canvas):
    QStartW,QStartH = gridToCoord(app,10,4)
    QStartW += app.gM + 2*app.screenMargin
    if app.solution == False:
        canvas.create_text(QStartW,QStartH,text='No path found',anchor='nw')
    elif app.cache != None and len(app.Q) == 0 and len(app.cache) != 0:
        canvas.create_text(QStartW,QStartH,text='Finished!',anchor='nw')
    else:
        for i in range(len(app.Q)):
            canvas.create_text(QStartW,QStartH+i*app.bH,text=f'Node: {app.Q[i]}',anchor='nw')

def BFS_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)
    drawQueueText(app,canvas)

