from cmu_112_graphics import *
from graphClass import *
from BFS import *


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


def getGridParams(app):
    gridRows = 10
    gridCols = 10
    boxHeight = app.gridHeight/gridRows
    boxWidth = app.gridWidth/gridCols
    gridMargin = 5
    return(gridRows,gridCols,boxHeight,boxWidth,gridMargin)

def getScreenParams(app):
    screenMargin = 5
    gridWidth = (app.width - 2*screenMargin)*3/4
    gridHeight = (app.height - 2*screenMargin)*3/4
    return (screenMargin,gridWidth,gridHeight)

def appStarted(app):
    app.screenMargin,app.gridWidth,app.gridHeight = getScreenParams(app)
    app.gR,app.gC,app.bH,app.bW,app.gM = getGridParams(app)
    app.grid = [[None]*app.gC for row in range(app.gR)]
    app.edgeMode = False
    app.editingMode = False
    app.prevNode = None
    app.nodes = []
    app.edges = []
    app.G = Graph(testGraph)
    app.step = 0
    blah,app.cache = BFS(app.G,A,F)
    setGraph(app)

def mousePressed(app,event):
    if inBounds(app,event.x,event.y) and app.editingMode:
        col = int((event.x - app.screenMargin + app.bW/2)/app.bW)
        row = int((event.y - 1/4*(app.height-2*app.screenMargin) + app.screenMargin + app.bH/2)/app.bH)
        if app.grid[col][row] != None:
            if app.edgeMode != True:
                app.edgeMode = True
                app.prevNode = app.grid[col][row]
            else:
                app.edgeMode = False
                app.edges.append((app.grid[col][row],app.prevNode))
        else:
            if app.edgeMode != True:
                app.edgeMode = True
                newNode = Node(col,row,f'{len(app.nodes)}')
                app.nodes.append(newNode)
                app.grid[col][row] = newNode
                app.prevNode = newNode
            else:
                app.edgeMode = False
                newNode = Node(col,row,f'{len(app.nodes)}')
                app.nodes.append(newNode)
                app.grid[col][row] = newNode
                app.edges.append((newNode,app.prevNode))


def inBounds(app,x,y):
    return ((app.screenMargin + app.bW/2 <= x <= app.screenMargin - app.bW/2 + app.gridWidth) and
    (1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.bH/2 <= y <= app.height - (app.screenMargin + app.bH/2)))

def keyPressed(app,event):
    if event.key == 's':
        if app.step < len(app.cache):
            state = app.cache[app.step]
            seen,path,current = state
            for node in app.nodes:
                if node == current:
                    node.color = 'green'
                elif node in seen:
                    node.color = 'grey'
            app.step += 1

def gridToCoord(app,x,y):
    coordX = x*app.bW + app.screenMargin + app.gM
    coordY = y*app.bH + 1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.gM
    return (coordX,coordY)

def setGraph(app):
    app.nodes = list(app.G.graph)
    seen = set()
    for node in app.G.graph:
        for neighbor in app.G.graph[node]:
            if neighbor not in seen:
                app.edges.append((node,neighbor))
        seen.add(node)
    print(app.edges)

def drawEdges(app,canvas):
    for edge in app.edges:
        n1,n2 = edge
        x1,y1 = gridToCoord(app,n1.x,n1.y)
        x2,y2 = gridToCoord(app,n2.x,n2.y)
        canvas.create_line(x1,y1,x2,y2)

def drawNodes(app,canvas):
    for node in app.nodes:
        cx,cy = gridToCoord(app,node.x,node.y)
        r = node.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=node.color)
        canvas.create_text(cx,cy,text=f'{node.label}')

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

def drawOtherGrid(app,canvas):
    width = app.bW
    height = app.bH
    margin = app.gM
    gridStartHeight = 1/4*(app.height-2*app.screenMargin) - app.screenMargin + height/2
    gridStartWidth = app.screenMargin + width/2
    for row in range(app.gR-1):
        for col in range(app.gC-1):
            canvas.create_rectangle(
                margin+gridStartWidth+width*col,
                margin+gridStartHeight+height*row,
                margin+gridStartWidth+width*(col+1),
                margin+gridStartHeight+height*(row+1))

def redrawAll(app,canvas):
    drawGrid(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)
    #drawOtherGrid(app,canvas)

    return

runApp(width=800,height=600)
