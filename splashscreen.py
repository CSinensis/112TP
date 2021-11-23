from cmu_112_graphics import *
from visualizeHelper import *

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

def ss_redrawAll(app,canvas):
    drawGrid(app,canvas)
    drawQueue(app,canvas)
    drawButtons(app,canvas)
    drawModes(app,canvas)
    return

