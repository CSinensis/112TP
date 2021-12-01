from cmu_112_graphics import *
from graphClass import *
from dijkstra import *
from visualizeHelper import *
# FILE FUNCTION: Dijkstra's visualization

def dijk_mousePressed(app,event):
    if app.G.graph != dict() and inForBounds(app,event.x,event.y) and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.G.graph != dict() and inBackBounds(app,event.x,event.y) and app.step > 0:
        app.step -= 1
        applyState(app)
    elif inCustomBounds(app,event.x,event.y):
        app.mode = 'create'
        resetCustom(app)
    elif inResetBounds(app,event.x,event.y):
        reset(app)
    else:
        toggleOptions(app,event.x,event.y)

def dijk_timerFired(app):
    if app.auto and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.cache != None and app.step < len(app.cache):
        app.auto = False

def dijk_keyPressed(app,event):
    if app.G.graph != dict() and event.key == 'Right' and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.G.graph != dict() and event.key == 'Left' and app.step > 0:
        app.step -= 1
        applyState(app)
    elif event.key == 'r':
        reset(app)

def applyState(app):
    if app.cache == None:
        app.solution,app.cache = dijkstra(app.G,app.G.start,app.G.end)
    if app.step < len(app.cache):
        state = app.cache[app.step]
        seen,costs,current,check,Q = state
        app.Q = Q[:6]
        edges = pathToEdges(app,costs,current)
        for node in app.nodes:
            if node == current:
                node.color = myGreen
            elif node in seen:
                node.color = 'grey'
            elif node == check and current != app.G.end:
                node.color = myBlue
            else:
                node.color = 'red3'
        for edge in app.edges:
            if edge.path in edges:
                edge.color = myGreen
            else:
                edge.color = 'black'

def pathToEdges(app,costs,current):
    edges = set()
    node = current
    while node != app.G.start:
        key = costs[node][1]
        edges.add((key,node))
        edges.add((node,key))
        node = key
    return edges

def drawQueueText(app,canvas):
    QStartW,QStartH = gridToCoord(app,10,4)
    QStartW += app.gM + 2*app.screenMargin
    if app.solution == False:
        canvas.create_text(QStartW,QStartH,text='No path found',anchor='nw')
    elif app.cache != None and len(app.Q) == 0 and app.step >= len(app.cache)-1:
        canvas.create_text(QStartW,QStartH,text='Finished!',anchor='nw')
    else:
        for i in range(len(app.Q)):
            canvas.create_text(QStartW,QStartH+i*app.bH,text=f'''Node: {app.Q[i][1]}\nCost: {int(app.Q[i][0])}''',anchor='nw')

def dijk_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawWeightedEdges(app,canvas)
    drawNodes(app,canvas)
    drawQueueText(app,canvas)