from cmu_112_graphics import *
from graphClass import *

def reset(app):
    if app.gMode == 'HC1':
        app.G,app.startNode,app.endNode = getHardcoded1()
    elif app.gMode == 'HC2':
        app.G,app.startNode,app.endNode = getHardcoded2()
    app.grid = [[None]*app.gC for row in range(app.gR)]
    app.edgeMode = False
    app.editingMode = True
    app.prevNode = None
    app.nodes = []
    app.edges = []
    app.step = 0
    app.cache = None
    app.Q = []
    app.auto = False
    setGraph(app)

def getHardcoded1():
    A = Node(4,2,'A')
    B = Node(3,4,'B')
    C = Node(5,4,'C')
    D = Node(7,4,'D')
    E = Node(4,6,'E')
    F = Node(6,6,'F')
    G = Node(7,8,'G')
    H = Node(3,7,'H')
    testGraph = {
        A:{B:2,C:4,D:3},
        B:{A:2,H:10},
        C:{A:4,E:5,F:2},
        D:{A:3,F:8},
        E:{C:5,H:6},
        F:{D:8,C:5,G:3},
        G:{F:3},
        H:{E:6,B:10}
    }
    return Graph(testGraph),A,H

def getHardcoded2():
    A = Node(4,2,'A')
    B = Node(3,4,'B')
    C = Node(5,4,'C')
    D = Node(7,4,'D')
    E = Node(4,6,'E')
    F = Node(6,6,'F')
    testGraph = {
        A:{B:2,C:4,D:3},
        B:{A:2},
        C:{A:4,E:5,F:2},
        D:{A:3,F:8},
        E:{C:5},
        F:{D:8,C:5}
    }
    return Graph(testGraph),A,F

def setGraph(app):
    app.nodes = list(app.G.graph)
    seen = set()
    for node in app.G.graph:
        for neighbor in app.G.graph[node]:
            if neighbor not in seen:
                newEdge = Edge(node,neighbor)
                newEdge.weight = app.G.graph[node][neighbor]
                app.edges.append(newEdge)
        seen.add(node)

def inBounds(app,x,y):
    return ((app.screenMargin + app.bW/2 <= x <= app.screenMargin - app.bW/2 + app.gridWidth) and
    (1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.bH/2 <= y <= app.height - (app.screenMargin + app.bH/2)))

def inForBounds(app,x,y):
    startW,startH,endW,endH = getForBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def inBackBounds(app,x,y):
    startW,startH,endW,endH = getBackBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def inAutoBounds(app,x,y):
    startW,startH,endW,endH = getAutoBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def inBFSBounds(app,x,y):
    startW,startH,endW,endH = getBFSModeBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def inDijkBounds(app,x,y):
    startW,startH,endW,endH = getDijkModeBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def gridToCoord(app,x,y):
    coordX = x*app.bW + app.screenMargin + app.gM
    coordY = y*app.bH + 1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.gM
    return (coordX,coordY)

def getModeBounds(app):
    startW,startH = app.screenMargin + app.gM,app.screenMargin + app.gM
    endW,endH = gridToCoord(app,3,-1)
    return startW,startH,endW,endH

def getBFSModeBounds(app):
    startW,startH,endW,endH = getModeBounds(app)
    midH = (startH + endH)/2
    return startW,midH,endW,endH

def getDijkModeBounds(app):
    startW,startH,endW,endH = getModeBounds(app)
    midH = (startH + endH)/2
    return startW,startH,endW,midH

def drawModes(app,canvas):
    startW,startH,endW,endH = getModeBounds(app)
    midH = (startH + endH)/2
    if app.mode == 'BFS':
        c1,c2 = 'green','grey'
    elif app.mode == 'dijk':
        c1,c2 = 'grey','green'
    else:
        c1,c2 = 'grey','grey'
    canvas.create_rectangle(startW,startH,endW,midH,outline='black',fill=c1)
    canvas.create_text((startW+endW)/2,(startH+midH)/2,text='BFS')
    canvas.create_rectangle(startW,midH,endW,endH,outline='black',fill=c2)
    canvas.create_text((startW+endW)/2,(midH+endH)/2,text="Dijkstra's")

def drawQueue(app,canvas):
    QStartW,QStartH = gridToCoord(app,10,4)
    QStartW += app.gM + app.screenMargin
    QEndH,QEndW = app.height-app.screenMargin-app.gM,app.width-app.screenMargin - app.gM
    canvas.create_rectangle(QStartW,QStartH,QEndW,QEndH,outline = 'grey')
    canvas.create_text((QStartW+QEndW)/2,QStartH,text='Queue',anchor='s')
    for i in range(len(app.Q)):
        canvas.create_text(QStartW,QStartH+i*app.bH,text=app.Q[i],anchor='nw')

def getForBounds(app):
    startW,startH = gridToCoord(app,10,0)
    startW += app.gM + app.screenMargin
    endW = app.width-app.screenMargin - app.gM
    fill,endH = gridToCoord(app,10,1)
    return (startW,startH,endW,endH)

def getBackBounds(app):
    startW,startH = gridToCoord(app,10,1)
    startW += app.gM + app.screenMargin
    endW = app.width-app.screenMargin - app.gM
    fill,endH = gridToCoord(app,10,2)
    return (startW,startH,endW,endH)

def getAutoBounds(app):
    startW,startH = gridToCoord(app,10,2)
    startW += app.gM + app.screenMargin
    endW = app.width-app.screenMargin - app.gM
    fill,endH = gridToCoord(app,10,3)
    return (startW,startH,endW,endH)

def drawStepForward(app,canvas):
    startW,startH,endW,endH = getForBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='purple')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Step Forwards')

def drawStepBackward(app,canvas):
    startW,startH,endW,endH = getBackBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='cyan')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Step Backwards')

def drawStepAuto(app,canvas):
    startW,startH,endW,endH = getAutoBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH,fill='pink')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Run Automatically')

def drawButtons(app,canvas):
    drawStepForward(app,canvas)
    drawStepBackward(app,canvas)
    drawStepAuto(app,canvas)

def drawGrid(app,canvas):
    width = app.bW
    height = app.bH
    margin = app.gM
    gridStartHeight = 1/4*(app.height-2*app.screenMargin) - app.screenMargin
    gridStartWidth = app.screenMargin
    for row in range(app.gR):
        for col in range(app.gC):
            canvas.create_rectangle(
                margin+gridStartWidth+width*col,
                margin+gridStartHeight+height*row,
                margin+gridStartWidth+width*(col+1),
                margin+gridStartHeight+height*(row+1),outline='grey')

# def drawOtherGrid(app,canvas):
#     width = app.bW
#     height = app.bH
#     margin = app.gM
#     gridStartHeight = 1/4*(app.height-2*app.screenMargin) - app.screenMargin + height/2
#     gridStartWidth = app.screenMargin + width/2
#     for row in range(app.gR-1):
#         for col in range(app.gC-1):
#             canvas.create_rectangle(
#                 margin+gridStartWidth+width*col,
#                 margin+gridStartHeight+height*row,
#                 margin+gridStartWidth+width*(col+1),
#                 margin+gridStartHeight+height*(row+1))