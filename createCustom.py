from cmu_112_graphics import *
from graphClass import *
from dijkstra import *
from visualizeHelper import *
from backendHelper import *
import random

def create_mousePressed(app,event):
    if inBounds(app,event.x,event.y):
        col = int((event.x - app.screenMargin + app.bW/2)/app.bW)
        row = int((event.y - 1/4*(app.height-2*app.screenMargin) + app.screenMargin + app.bH/2)/app.bH)
        if app.grid[col][row] != None:
            if app.setStart == True:
                app.setStart = False
                app.customGraph.start = app.grid[col][row]
            elif app.setEnd == True:
                app.setEnd = False
                app.customGraph.end = app.grid[col][row]
            elif app.edgeMode != True:
                app.edgeMode = True
                app.prevNode = app.grid[col][row]
            else:
                app.edgeMode = False
                newEdge = Edge(app.grid[col][row],app.prevNode)
                app.edges.append(newEdge)
                curNode = app.grid[col][row]
                app.customGraph.addEdge(curNode,app.prevNode,h(curNode,app.prevNode)+random.randrange(1,5))
        else:
            addToGraph(app,row,col)
    elif inCustomBounds(app,event.x,event.y):
        app.mode = 'BFS'
        if app.customGraph.graph != dict() and app.customGraph.end == None:
            app.customGraph.end = app.nodes[-1]
        app.gMode = 'custom'
        reset(app)
    elif inResetBounds(app,event.x,event.y):
        resetCustom(app)
    elif inHomeBounds(app,event.x,event.y):
        app.mode = 'ss'
        splashStarted(app)
    else:
        toggleCustom(app,event.x,event.y)

def addToGraph(app,row,col):
    newNode = Node(col,row,f'{len(app.nodes)}')
    app.nodes.append(newNode)
    if app.customGraph.start == None:
        app.customGraph.start = app.nodes[0]
    app.grid[col][row] = newNode
    if app.edgeMode:
        app.edgeMode = False
        newEdge = Edge(newNode,app.prevNode)
        app.edges.append(newEdge)
        app.customGraph.addEdge(newNode,app.prevNode,h(newNode,app.prevNode)+random.randrange(1,5))

def toggleCustom(app,x,y):
    if inForBounds(app,x,y):
        app.setStart = True
    elif inBackBounds(app,x,y):
        app.setEnd = True
    elif inAutoBounds(app,x,y) and app.customGraph.graph != dict():
        if app.customGraph.end == None:
            app.customGraph.end = app.nodes[-1]
        app.savedGraphs.append(copy.deepcopy(app.customGraph))

def create_keyPressed(app,event):
    if event.key == 's':
        if app.customGraph.end == None:
            app.customGraph.end = app.nodes[-1]
        app.savedGraphs.append(copy.deepcopy(app.customGraph))
    elif event.key == 'g':
        app.mode = 'gal'
        galStarted(app)
    elif event.key == 'q':
        app.setStart = True
    elif event.key == 'w':
        app.setEnd = True

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

def drawCustomGraphParams(app,canvas):
    startH = 1/4*(app.height-2*app.screenMargin) - app.screenMargin
    startW = 2*app.screenMargin
    canvas.create_text(startW,startH,text=f'Graph Details - Start Node: {app.customGraph.start} \t End Node: {app.customGraph.end}',anchor='sw')

def drawSetStart(app,canvas):
    startW,startH,endW,endH = getForBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='purple')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Set Start Node')

def drawSetEnd(app,canvas):
    startW,startH,endW,endH = getBackBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='cyan')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Set End Node')

def drawSave(app,canvas):
    startW,startH,endW,endH = getAutoBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='pink')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Save to Gallery')

def drawCustomButtons(app,canvas):
    drawSetStart(app,canvas)
    drawSetEnd(app,canvas)
    drawSave(app,canvas)


def create_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)
    drawCustomGraphParams(app,canvas)
    drawCustomButtons(app,canvas)