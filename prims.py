from cmu_112_graphics import *
from visualizeHelper import *
from graphClass import *
import random
# FILE FUNCTION: Runs and visualizes maze generation using prim's algorithm
"""
References:
Wikipedia:
https://en.wikipedia.org/wiki/Prim%27s_algorithm
StackExchange (mainly the first responder's):
https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-maze-using-prims-algorithm
Prim's Algorithm in 2 minutes:
https://www.youtube.com/watch?v=cplfcGZmX7I
Maze Generation with Prim's Algorithm (mostly for visualization inspiration):
https://www.youtube.com/watch?v=Kyoep91w7NE
"""
def prim_mousePressed(app,event):
    if inHomeBounds(app,event.x,event.y):
        app.mode = 'ss'
        splashStarted(app)
    else: 
        toggleMaze(app,event.x,event.y+app.screenMargin/2)

def toggleMaze(app,x,y):
    if inForBounds(app,x,y) and (app.states == None or app.index < len(app.states)):
        app.index += 1
        applyState(app)
    elif inBackBounds(app,x,y) and app.index > 0:
        app.index -= 1
        applyState(app)
    elif inAutoBounds(app,x,y):
        app.mazeAuto = not app.mazeAuto

def prim_keyPressed(app,event):
    if event.key == 'Right' and (app.states == None or app.index < len(app.states)):
        app.index += 1
        applyState(app)
    elif event.key == 'Left' and app.index > 0:
        app.index -= 1
        applyState(app)

def prim_timerFired(app):
    if app.mazeAuto:
        app.index += 1
        applyState(app)

def applyState(app):
    if app.states == None:
        app.states = prim(app)
    if app.index < len(app.states):
        app.curState = app.states[app.index]

def drawState(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            if app.curState != None:
                app.curState[row][col].draw(app,canvas)

def drawBackground(app,canvas):
    canvas.create_rectangle(app.screenMargin,app.screenMargin,
    app.width-app.screenMargin,app.height-app.screenMargin,fill=myBlue,width=0)
    canvas.create_rectangle(2*app.screenMargin,app.height/4,app.width-2*app.screenMargin-10*app.s,app.height-2*app.screenMargin,fill='black')
    canvas.create_rectangle(app.screenMargin,app.screenMargin,
    app.width-app.screenMargin,app.screenMargin + app.bannerH,fill=myGreen,width=0)
    canvas.create_text(0.9*app.width/2,app.screenH/8 + app.screenMargin,text=('''Maze Generation Visualizer\n Prim's Algorithm'''), font="Arial 50 bold",justify='left')

def prim(app):
    startR,startC = random.randrange(1,app.rows-1,2),random.randrange(1,app.cols-1,2)
    app.maze[startR][startC].role = 'white'
    addFrontier(app,startR,startC)
    states = [copy.deepcopy(app.maze)]
    while len(app.frontier) > 0:
        i = random.randrange(0,len(app.frontier))
        frontCell = app.frontier.pop(i)
        frontCell.role = 'white'
        neighbors = getNeighbors(app,frontCell)
        j = random.randrange(0,len(neighbors))
        backCell = neighbors[j]
        moveR,moveC = ((frontCell.row - backCell.row)/2,(frontCell.col - backCell.col)/2)
        app.maze[backCell.row+int(moveR)][backCell.col+int(moveC)].role = 'white'
        cleanFrontier(app)
        addFrontier(app,frontCell.row,frontCell.col)
        states.append(copy.deepcopy(app.maze))
    return states

def cleanFrontier(app):
    for cell in app.frontier:
        if cell.role == 'white':
            app.frontier.remove(cell)

def addFrontier(app,startR,startC):
    dirs = [(-2,0),(0,-2),(2,0),(0,2)]
    for d in dirs:
        dr,dc = d
        if inMazeBounds(app,startR+dr,startC+dc) and app.maze[startR+dr][startC+dc].role == 'black':
            app.frontier.append(app.maze[startR+dr][startC+dc])
            app.maze[startR+dr][startC+dc].role = myGreen

def inMazeBounds(app,row,col):
    if 0 < row < app.rows-1 and 0 < col < app.cols-1:
        return True
    return False

def getNeighbors(app,cell):
    neighbors = []
    dirs = [(-2,0),(0,-2),(2,0),(0,2)]
    row,col = cell.row,cell.col
    for d in dirs:
        dr,dc = d
        if inMazeBounds(app,row+dr,col+dc) and app.maze[row+dr][col+dc].role == 'white':
            neighbors.append(app.maze[row+dr][col+dc])
    return neighbors

def drawSetStart(app,canvas):
    startW,startH,endW,endH = getForBounds(app)
    startH += app.screenMargin/2
    endH += app.screenMargin/2
    canvas.create_rectangle(startW,startH,endW,endH,fill='MediumPurple3')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Step Forwards')

def drawSetEnd(app,canvas):
    startW,startH,endW,endH = getBackBounds(app)
    startH += app.screenMargin/2
    endH += app.screenMargin/2
    canvas.create_rectangle(startW,startH,endW,endH,fill='medium turquoise')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Step Backwards')

def drawSave(app,canvas):
    startW,startH,endW,endH = getAutoBounds(app)
    startH += app.screenMargin/2
    endH += app.screenMargin/2
    canvas.create_rectangle(startW,startH,endW,endH,fill='light coral')
    canvas.create_text((startW+endW)/2,(startH+endH)/2,text='Run Automatically')

def drawCustomButtons(app,canvas):
    drawSetStart(app,canvas)
    drawSetEnd(app,canvas)
    drawSave(app,canvas)

def drawKey(app,canvas):
    StartW,StartH = gridToCoord(app,10,4)
    StartW += app.gM + app.screenMargin
    EndH,EndW = app.height-app.screenMargin-app.gM,app.width-app.screenMargin - app.gM
    canvas.create_rectangle(StartW,StartH,EndW,EndH)
    canvas.create_text((StartW+EndW)/2,StartH,text='Key',anchor='n',font='Arial 15')
    canvas.create_text(StartW+app.screenMargin,StartH+2*app.s,text='Black - Maze wall',anchor='nw')
    canvas.create_text(StartW+app.screenMargin,StartH+5*app.s,text='White - Maze passage',anchor='nw')
    canvas.create_text(StartW+app.screenMargin,StartH+8*app.s,text='Green - Passage frontier',anchor='nw')

def prim_redrawAll(app,canvas):
    drawBackground(app,canvas)
    if app.curState != None:
        drawState(app,canvas)
    drawHome(app,canvas)
    drawCustomButtons(app,canvas)
    drawKey(app,canvas)
