from cmu_112_graphics import *
from graphClass import *
from aStar import *
from visualizeHelper import *

def aStar_mousePressed(app,event):
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

def aStar_timerFired(app):
    if app.auto and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.cache != None and app.step < len(app.cache):
        app.auto = False

def applyState(app):
    if app.cache == None:
        print(app.G,app.G.start,app.G.end)
        app.solution,app.cache = aStar(app.G,app.G.start,app.G.end)
    if app.step < len(app.cache):
        state = app.cache[app.step]
        print(state)
        seen,costs,current,check,Q = state
        edges = pathToEdges(app,costs,current)
        app.Q = Q[:6]
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
        key = costs[node][3]
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
            canvas.create_text(QStartW,QStartH+i*app.bH,text=f'''Node: {app.Q[i][3]}\tH-Cost:{int(app.Q[i][1])}\nTotal Cost: {int(app.Q[i][0])}''',anchor='nw')

def aStar_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawWeightedEdges(app,canvas)
    drawNodes(app,canvas)
    drawQueueText(app,canvas)

