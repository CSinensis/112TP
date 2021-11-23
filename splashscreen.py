from cmu_112_graphics import *
from visualizeHelper import *

def splashStarted(app):
    app.sMargin = 100
    app.optStartW,app.optStartH = app.sMargin,3*app.height/4 - 50 + app.screenMargin
    app.optEndW,app.optEndH = app.width-app.sMargin,3*app.height/4 + 50 + app.screenMargin
    app.optBoxW = (app.optEndW-app.optStartW-2*app.screenMargin)/3
    
def ss_mousePressed(app,event):
    if inOptCustom(app,event.x,event.y):
        app.mode = 'create'
        resetCustom(app)
    elif inOptVis(app,event.x,event.y):
        app.mode = 'BFS'
        app.cache = None
        reset(app)

def ss_keyPressed(app,event):
    return

def inOptCustom(app,x,y):
    w1,h1,w2,h2 = getOptCustomBounds(app)
    return True if ((w1 <= x <= w2) and (h1 <= y <= h2)) else False

def inOptVis(app,x,y):
    w1,h1,w2,h2 = getOptVisBounds(app)
    return True if ((w1 <= x <= w2) and (h1 <= y <= h2)) else False

def inOptExtra(app,x,y):
    return

def drawOptBound(app,canvas):
    canvas.create_rectangle(app.optStartW,app.optStartH,app.optEndW,app.optEndH,fill=myYellow)

def getOptCustomBounds(app):
    w1,h1 = app.optStartW,app.optStartH
    w2,h2 = w1 + app.optBoxW,app.optEndH
    return (w1,h1,w2,h2)

def drawOptCustom(app,canvas):
    w1,h1,w2,h2 = getOptCustomBounds(app)
    canvas.create_rectangle(w1,h1,w2,h2,fill=myYellow)
    canvas.create_text((w1+w2)/2,(h1+h2)/2,text='Create a Graph')

def getOptVisBounds(app):
    w1,h1 = app.screenMargin + app.optStartW + app.optBoxW,app.optStartH
    w2,h2 = w1 + app.optBoxW,app.optEndH
    return (w1,h1,w2,h2)

def drawOptVis(app,canvas):
    w1,h1,w2,h2 = getOptVisBounds(app)
    canvas.create_rectangle(w1,h1,w2,h2,fill=myYellow)
    canvas.create_text((w1+w2)/2,(h1+h2)/2,text='Begin Visualization')

def getOptExtraBounds(app):
    w1,h1 = 2*app.screenMargin + app.optStartW + 2*app.optBoxW,app.optStartH
    w2,h2 = w1 + app.optBoxW,app.optEndH
    return (w1,h1,w2,h2)

def drawOptExtra(app,canvas):
    w1,h1,w2,h2 = getOptExtraBounds(app)
    canvas.create_rectangle(w1,h1,w2,h2,fill=myYellow)
    canvas.create_text((w1+w2)/2,(h1+h2)/2,text='yeet')

def ss_redrawAll(app,canvas):
    canvas.create_rectangle(0+app.screenMargin,0+app.screenMargin,
    app.width-app.screenMargin,app.height-app.screenMargin,fill=myBlue)
    canvas.create_rectangle(app.sMargin,app.height/2-150,app.width-app.sMargin,app.height/2+50,fill=myYellow)
    canvas.create_text(app.width/2,app.height/2,text=('''Welcome to 
Pathfinding Visualizer'''), font="Arial 50 bold",anchor = 's',justify='center')
    #drawOptBound(app,canvas)
    drawOptCustom(app,canvas)
    drawOptVis(app,canvas)
    drawOptExtra(app,canvas)


