from cmu_112_graphics import *
from graphClass import *
# import pygame
# from pygame.locals import *
# from pygame import mixer
# pygame.mixer.init()

# def play():
#     musicPath = '/Users/nanyu/Documents/GitHub/112TP/Xue Mao Jiao - Xiao Pan Pan & Xiao Feng Feng.mp3'
#     pygame.mixer.music.load(musicPath)
#     pygame.mixer.music.play(-1)

def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

myBlue = rgbString(0, 159, 183)
myYellow = rgbString(254, 215, 102)
myGreen = rgbString(104, 163, 87)
myRed = rgbString(109, 33, 60)

def resetCustom(app):
    app.customGraph = Graph(dict())
    app.grid = [[None]*app.gC for row in range(app.gR)]
    app.edgeMode = False
    app.prevNode = None
    app.nodes = []
    app.edges = []
    # app.step = 0
    # app.cache = None
    app.Q = []
    # app.auto = False
    app.customMessage = '''Click here to exit 
    editing mode'''

def reset(app):
    if app.gMode == 'HC1':
        app.G = getHardcoded1()
        print("YE",app.G.start,app.G.end)
    elif app.gMode == 'HC2':
        app.G = getHardcoded2()
    elif app.gMode == 'custom':
        app.G = copy.deepcopy(app.customGraph)
        print(app.G.graph)
        print("YE",app.G.start,app.G.end)
    app.grid = [[None]*app.gC for row in range(app.gR)]
    # app.edgeMode = False
    # app.prevNode = None
    app.nodes = []
    app.edges = []
    app.step = 0
    app.cache = None
    app.Q = []
    app.auto = False
    app.customMessage = ('''Click here to create
    a custom graph''')
    setGraph(app)

def galStarted(app):
    app.galM = 2*app.screenMargin
    app.bannerH = (app.height - 2*app.screenMargin)/5 
    app.screenW = app.width - 2*app.screenMargin
    app.screenH = (app.height - 2*app.screenMargin) - app.bannerH
    app.galW = (app.screenW - 4*app.galM)/6
    app.galH = (app.screenH - 3*app.galM)/4
    app.bounds = getGalBounds(app)
    app.miniW = app.galW/5
    app.miniH = (app.galH - 20)/5
    return

def getGalBounds(app):
    bounds = dict()
    index = 0
    for i in range(2):
        for j in range(3):
            cx,cy = app.screenMargin + app.galM + app.galW + (j)*(2*app.galW+app.galM),app.screenMargin + app.galM + app.galH + (i)*(2*app.galH+app.galM) + app.bannerH
            bounds[index] = (cx-app.galW,cy-app.galH,cx+app.galW,cy+app.galH)
            index += 1
    return bounds

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
    G = Graph(testGraph)
    G.start = A
    G.end = H
    print("NE",G.start,G.end)
    return G

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
    G = Graph(testGraph)
    G.start = A
    G.end = F
    return G

def getHardcoded3():
    largerTestGraph = {
    'X':{'E':4,'A':7,'B':2,'C':3},
    'A':{'X':7,'B':3,'D':4},
    'B':{'X':2,'A':3,'D':4,'H':5},
    'C':{'X':3,'L':2},
    'D':{'A':4,'B':4,'F':1},
    'E':{'X':4},
    'F':{'D':1,'H':3},
    'G':{'H':2,'Y':2},
    'H':{'G':2,'B':5,'F':3},
    'I':{'L':4,'J':6,'K':4},
    'J':{'L':1,'I':6},
    'K':{'I':4,'Y':5},
    'L':{'C':2,'I':4,'J':1},
    'Y':{'G':2,'K':5},
}

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

def toggleOptions(app,x,y):
    if inAutoBounds(app,x,y):
        app.auto = not app.auto
    elif inDijkBounds(app,x,y):
        app.mode = 'dijk'
        app.cache = None
        reset(app)
    elif inBFSBounds(app,x,y):
        app.mode = 'BFS'
        app.cache = None
        reset(app)
    elif inAStarBounds(app,x,y):
        app.mode = 'aStar'
        app.cache = None
        reset(app)
    elif inHC1Bounds(app,x,y):
        app.gMode = 'HC1'
        reset(app)
    elif inHC2Bounds(app,x,y):
        app.gMode = 'HC2'
        reset(app)

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

def inAStarBounds(app,x,y):
    startW,startH,endW,endH = getAStarModeBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def inCustomBounds(app,x,y):
    startW,startH,endW,endH = getCustomBounds(app)
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
    midH1 = (startH + (endH-startH)/3)
    return startW,startH,endW,midH1

def getDijkModeBounds(app):
    startW,startH,endW,endH = getModeBounds(app)
    midH1 = (startH + (endH-startH)/3)
    midH2 = (startH + 2*(endH-startH)/3)
    return startW,midH1,endW,midH2

def getAStarModeBounds(app):
    startW,startH,endW,endH = getModeBounds(app)
    midH2 = (startH + 2*(endH-startH)/3)
    return startW,midH2,endW,endH

def getCustomBounds(app):
    startW,startH = app.screenMargin + app.gM + app.bW*8,app.screenMargin + app.gM
    endW,endH = gridToCoord(app,10,-1)
    return startW,startH,endW,endH

def drawCustom(app,canvas):
    startW,startH,endW,endH = getCustomBounds(app)
    if app.mode == 'create':
        c = myGreen
    else:
        c = 'grey'
    canvas.create_rectangle(startW,startH,endW,endH,fill=c)
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text=app.customMessage)

def drawModes(app,canvas):
    startW,startH,endW,endH = getModeBounds(app)
    dH = (endH-startH)/3
    if app.mode == 'BFS':
        c1,c2,c3 = myGreen,'grey','grey'
    elif app.mode == 'dijk':
        c1,c2,c3 = 'grey',myGreen,'grey'
    elif app.mode == 'aStar':
        c1,c2,c3 = 'grey','grey',myGreen
    else:
        c1,c2,c3 = 'grey','grey','grey'
    canvas.create_rectangle(startW,startH,endW,startH+dH,outline='black',fill=c1)
    canvas.create_text((startW+endW)/2,(startH+startH+dH)/2,text='BFS')
    canvas.create_rectangle(startW,startH+dH,endW,startH+2*dH,outline='black',fill=c2)
    canvas.create_text((startW+endW)/2,(2*startH+3*dH)/2,text="Dijkstra's")
    canvas.create_rectangle(startW,startH+2*dH,endW,endH,outline='black',fill=c3)
    canvas.create_text((startW+endW)/2,(startH+2*dH+endH)/2,text="A*")

def getOptBounds(app):
    startW,startH = app.screenMargin + app.gM + 4*(app.bW),app.screenMargin + app.gM
    endW,endH = gridToCoord(app,7,-1)
    return startW,startH,endW,endH

def inHC1Bounds(app,x,y):
    startW,startH,endW,endH = getHC1Bounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def inHC2Bounds(app,x,y):
    startW,startH,endW,endH = getHC2Bounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def getHC1Bounds(app):
    startW,startH,endW,endH = getOptBounds(app)
    midH = (startH + endH)/2
    return startW,startH,endW,midH

def getHC2Bounds(app):
    startW,startH,endW,endH = getOptBounds(app)
    midH = (startH + endH)/2
    return startW,midH,endW,endH

def drawGraphOptions(app,canvas):
    startW,startH,endW,midH = startW,startH,endW,endH = getOptBounds(app)
    midH = (startH + endH)/2
    if app.gMode == 'HC1':
        c1,c2 = myGreen,'grey'
    elif app.gMode == 'HC2':
        c1,c2 = 'grey',myGreen
    else:
        c1,c2 = 'grey','grey'
    canvas.create_rectangle(startW,startH,endW,midH,outline='black',fill=c1)
    canvas.create_text((startW+endW)/2,(startH+midH)/2,text='Hardcoded 1')
    canvas.create_rectangle(startW,midH,endW,endH,outline='black',fill=c2)
    canvas.create_text((startW+endW)/2,(midH+endH)/2,text='Hardcoded 2')

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

def inResetBounds(app,x,y):
    startW,startH,endW,endH = getResetBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def getResetBounds(app):
    startW,startH = 2*(app.screenMargin + app.gM) + app.bW*10,app.screenMargin + app.gM
    endW = app.width-app.screenMargin - app.gM
    fill,endH = gridToCoord(app,10,-1)
    return startW,startH,endW,endH

def drawReset(app,canvas):
    startW,startH,endW,endH = getResetBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH)
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Reset')    

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

def drawAll(app,canvas):
    drawGrid(app,canvas)
    drawQueue(app,canvas)
    drawButtons(app,canvas)
    drawModes(app,canvas)
    drawGraphOptions(app,canvas)
    drawCustom(app,canvas)
    drawReset(app,canvas)

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