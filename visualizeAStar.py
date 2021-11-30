from cmu_112_graphics import *
from graphClass import *
from aStar import *
from visualizeHelper import *

def aStar_mousePressed(app,event):
    if inForBounds(app,event.x,event.y) and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif inBackBounds(app,event.x,event.y) and app.step > 0:
        app.step -= 1
        applyState(app)
    elif inCustomBounds(app,event.x,event.y):
        app.mode = 'create'
        resetCustom(app)
    elif inResetBounds(app,event.x,event.y):
        reset(app)
    else:
        toggleOptions(app,event.x,event.y)

    
def aStar_keyPressed(app,event):
    if event.key == 'Right' and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif event.key == 'Left' and app.step > 0:
        app.step -= 1
        applyState(app)
    elif event.key == 't':
        app.mode = 'BFS'
        app.cache = None
        reset(app)
    elif event.key == 'r':
        reset(app)
    elif event.key == 'n':
        print("HERE")
        app.gMode = 'HC2'
        reset(app)

def aStar_timerFired(app):
    if app.auto and (app.cache == None or app.step < len(app.cache)):
        app.step += 1
        applyState(app)
    elif app.cache != None and app.step < len(app.cache):
        app.auto = False

def applyState(app):
    if app.cache == None:
        print(app.G,app.G.start,app.G.end)
        blah,app.cache = aStar(app.G,app.G.start,app.G.end)
    if app.step < len(app.cache):
        state = app.cache[app.step]
        print(state)
        seen,costs,current,check,Q = state
        edges = pathToEdges(app,costs,current)
        app.Q = Q
        for node in app.nodes:
            if node == current:
                node.color = myGreen
            elif node in seen:
                node.color = 'grey'
            elif node == check and current != app.G.end:
                node.color = myBlue
            else:
                node.color = 'red'
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
        node = key
    return edges

def drawEdges(app,canvas):
    for edge in app.edges:
        n1,n2 = edge.path
        x1,y1 = gridToCoord(app,n1.x,n1.y)
        x2,y2 = gridToCoord(app,n2.x,n2.y)
        avgX,avgY = (x1+x2)/2,(y1+y2)/2
        canvas.create_line(x1,y1,x2,y2,fill=edge.color)
        canvas.create_text(avgX,avgY,text=f'{edge.weight}')

def drawNodes(app,canvas):
    for node in app.nodes:
        cx,cy = gridToCoord(app,node.x,node.y)
        r = node.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=node.color)
        canvas.create_text(cx,cy,text=f'{node.label}')

def aStar_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)

    #drawOtherGrid(app,canvas)
