from cmu_112_graphics import *
from graphClass import *
from startingParams import *
# import pygame
# from pygame.locals import *
# from pygame import mixer
# pygame.mixer.init()

# def play():
#     musicPath = '/Users/nanyu/Documents/GitHub/112TP/Xue Mao Jiao - Xiao Pan Pan & Xiao Feng Feng.mp3'
#     pygame.mixer.music.load(musicPath)
#     pygame.mixer.music.play(-1)

def toggleOptions(app,x,y):
    if app.G.graph != dict() and inAutoBounds(app,x,y):
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
    elif inHomeBounds(app,x,y):
        app.mode = 'ss'
        splashStarted(app)

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
    canvas.create_text((startW+endW)/2,(startH+midH)/2,text='Sample Graph 1')
    canvas.create_rectangle(startW,midH,endW,endH,outline='black',fill=c2)
    canvas.create_text((startW+endW)/2,(midH+endH)/2,text='Sample Graph 2')

def drawQueueBox(app,canvas):
    QStartW,QStartH = gridToCoord(app,10,4)
    QStartW += app.gM + app.screenMargin
    QEndH,QEndW = app.height-app.screenMargin-app.gM,app.width-app.screenMargin - app.gM
    canvas.create_rectangle(QStartW,QStartH,QEndW,QEndH,outline = 'grey')
    canvas.create_text((QStartW+QEndW)/2,QStartH,text='Queue',anchor='s')

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
    endW = (app.width + app.screenMargin + app.gM)/2 + app.bW*5 - app.screenMargin
    fill,endH = gridToCoord(app,10,-1)
    return startW,startH,endW,endH

def drawReset(app,canvas):
    startW,startH,endW,endH = getResetBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH)
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Reset')

def inHomeBounds(app,x,y):
    startW,startH,endW,endH = getHomeBounds(app)
    return True if ((startW <= x <= endW) and (startH <= y <= endH)) else False

def getHomeBounds(app):
    startW,startH = (app.width + 3*app.screenMargin + app.gM)/2 + app.bW*5,app.screenMargin + app.gM
    endW = (app.width - app.screenMargin - app.gM)
    fill,endH = gridToCoord(app,10,-1)
    return startW,startH,endW,endH

def drawHome(app,canvas):
    startW,startH,endW,endH = getHomeBounds(app)
    canvas.create_rectangle(startW,startH,endW,endH)
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Home')     

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

def drawGraphParams(app,canvas):
    startH = 1/4*(app.height-2*app.screenMargin) - app.screenMargin
    startW = 2*app.screenMargin
    canvas.create_text(startW,startH,text=f'Graph Details - Start Node: {app.G.start} \t End Node: {app.G.end}',anchor='sw')

def drawAll(app,canvas):
    drawGrid(app,canvas)
    drawModes(app,canvas)
    drawQueueBox(app,canvas)
    drawGraphOptions(app,canvas)
    drawCustom(app,canvas)
    drawReset(app,canvas)
    drawHome(app,canvas)
    if app.mode != 'create':
        drawGraphParams(app,canvas)
        drawButtons(app,canvas)

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