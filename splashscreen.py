from cmu_112_graphics import *
from visualizeHelper import *

def splashStarted(app):
    app.sMargin = 100
    app.optStartW,app.optStartH = app.sMargin,3*app.height/4 - 50 + app.screenMargin
    app.optEndW,app.optEndH = app.width-app.sMargin,3*app.height/4 + 50 + app.screenMargin

def ss_mousePressed(app,event):
    if inDijkBounds(app,event.x,event.y):
        app.mode = 'BFS'
        app.cache = None
        reset(app)
    elif inBFSBounds(app,event.x,event.y):
        app.mode = 'dijk'
        app.cache = None
        reset(app)

def ss_keyPressed(app,event):
    return

def drawBoxes(app,canvas):
    canvas.create_rectangle(app.optStartW,app.optStartH,app.optEndW,app.optEndH,fill=myYellow)

def ss_redrawAll(app,canvas):
    canvas.create_rectangle(0+app.screenMargin,0+app.screenMargin,
    app.width-app.screenMargin,app.height-app.screenMargin,fill=myBlue)
    canvas.create_rectangle(app.sMargin,app.height/2-150,app.width-app.sMargin,app.height/2+50,fill=myYellow)
    canvas.create_text(app.width/2,app.height/2,text=('''Welcome to 
Pathfinding Visualizer'''), font="Arial 50 bold",anchor = 's',justify='center')
    drawBoxes(app,canvas)


