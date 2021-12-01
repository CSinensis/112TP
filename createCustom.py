from cmu_112_graphics import *
from graphClass import *
from visualizeHelper import *
from backendHelper import *
import random

def create_mousePressed(app,event):
    if inBounds(app,event.x,event.y):
        col = int((event.x - app.screenMargin + app.bW/2)/app.bW)
        row = int((event.y - 1/4*(app.height-2*app.screenMargin) + app.screenMargin + app.bH/2)/app.bH)
        if app.grid[col][row] != None:
            if app.setStart == True or app.setEnd == True:
                setEdgeNodes(app,app.grid[col][row])
            elif app.edgeMode != True:
                app.edgeMode = True
                app.prevNode = app.grid[col][row]
            else:
                addEdgeToGraph(app,app.grid[col][row])
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
    elif inOptBounds(app,event.x,event.y):
        app.mode = 'img'
        resetCustom(app)
        app.customGraph.url = app.getUserInput('Enter URL for image:')
        if app.customGraph.url == None:
            app.mode = 'create'
            resetCustom(app)
        else:
            customImgStarted(app)
    else:
        toggleCustom(app,event.x,event.y)

def setEdgeNodes(app,node):
    if app.setStart == True:
        app.setStart = False
        app.customGraph.start = node
    elif app.setEnd == True:
        app.setEnd = False
        app.customGraph.end = node

def addEdgeToGraph(app,node):
    app.edgeMode = False
    newEdge = Edge(node,app.prevNode)
    app.edges.append(newEdge)
    curNode = node
    app.customGraph.addEdge(curNode,app.prevNode,h(curNode,app.prevNode)+random.randrange(1,5))

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
        if len(app.savedGraphs) < 6:
            if app.customGraph.end == None:
                app.customGraph.end = app.nodes[-1]
            app.savedGraphs.append(copy.deepcopy(app.customGraph))
            app.customQText = 'Graph saved to gallery'
        else:
            app.customQText = 'Already have 6 graphs'

def create_keyPressed(app,event):
    if event.key == 'u':
        app.mode = 'img'
        resetCustom(app)
        app.customGraph.url = app.getUserInput('Enter URL for image:')
        if app.customGraph.url == None:
            app.mode = 'create'
            resetCustom(app)
        else:
            customImgStarted(app)

def drawCustomGraphParams(app,canvas):
    startH = 1/4*(app.height-2*app.screenMargin) - app.screenMargin
    startW = 2*app.screenMargin
    canvas.create_text(startW,startH,text=f'Graph Details - Start Node: {app.customGraph.start} \t End Node: {app.customGraph.end}',anchor='sw')

def drawSetStart(app,canvas):
    startW,startH,endW,endH = getForBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='MediumPurple3')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Set Start Node')

def drawSetEnd(app,canvas):
    startW,startH,endW,endH = getBackBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='medium turquoise')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Set End Node')

def drawSave(app,canvas):
    startW,startH,endW,endH = getAutoBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='light coral')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Save to Gallery')

def drawCustomButtons(app,canvas):
    drawSetStart(app,canvas)
    drawSetEnd(app,canvas)
    drawSave(app,canvas)

def drawCustomQText(app,canvas):
    QStartW,QStartH = gridToCoord(app,10,4)
    QStartW += app.gM + 2*app.screenMargin
    canvas.create_text(QStartW,QStartH,text=app.customQText,anchor='nw')

def drawImgOpt(app,canvas):
    startW,startH,endW,endH = getOptBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='grey70')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Click here to\nimport image')

def create_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawGrid(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)
    drawCustomGraphParams(app,canvas)
    drawCustomButtons(app,canvas)
    drawCustomQText(app,canvas)
    drawImgOpt(app,canvas)
