from cmu_112_graphics import *

class Node(object):
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def __repr__(self):
        return f'x:{self.cx},y:{self.cy}'

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
    app.nodes = []

def mousePressed(app,event):
    if ((app.screenMargin + app.bW/2 <= event.x <= app.screenMargin - app.bW/2 + app.gridWidth) and
    (1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.bH/2 <= event.y <= app.height - (app.screenMargin + app.bH/2))):
        col = int((event.x - app.screenMargin + app.bW/2)/app.bW)
        row = int((event.y - 1/4*(app.height-2*app.screenMargin) + app.screenMargin + app.bH/2)/app.bH)
        app.nodes.append(Node(col,row,10))

def drawNodes(app,canvas):
    for node in app.nodes:
        cx = node.x*app.bW + app.screenMargin + app.gM
        cy = node.y*app.bH + 1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.gM
        r = node.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill='red')

def drawGrid(app,canvas):
    width = app.bW
    height = app.bH
    margin = app.gM
    gridStartHeight = 1/4*(app.height-2*app.screenMargin) - app.screenMargin
    gridStartWidth = app.screenMargin
    for row in range(app.gR):
        for col in range(app.gC):
            # canvas.create_rectangle(
            #     margin+gridStartHeight+height*row,
            #     margin+gridStartWidth+width*col,
            #     margin+gridStartHeight+height*(row+1),
            #     margin+gridStartWidth+width*(col+1))
            canvas.create_rectangle(
                margin+gridStartWidth+width*col,
                margin+gridStartHeight+height*row,
                margin+gridStartWidth+width*(col+1),
                margin+gridStartHeight+height*(row+1))

def drawOtherGrid(app,canvas):
    width = app.bW
    height = app.bH
    margin = app.gM
    gridStartHeight = 1/4*(app.height-2*app.screenMargin) - app.screenMargin + height/2
    gridStartWidth = app.screenMargin + width/2
    for row in range(app.gR-1):
        for col in range(app.gC-1):
            # canvas.create_rectangle(
            #     margin+gridStartHeight+height*row,
            #     margin+gridStartWidth+width*col,
            #     margin+gridStartHeight+height*(row+1),
            #     margin+gridStartWidth+width*(col+1))
            canvas.create_rectangle(
                margin+gridStartWidth+width*col,
                margin+gridStartHeight+height*row,
                margin+gridStartWidth+width*(col+1),
                margin+gridStartHeight+height*(row+1))

# 5 + 152.5 + app.gridHeight/app.Rows * 100
# 157.5 + 442.5/10 * 11
def redrawAll(app,canvas):
    drawGrid(app,canvas)
    drawNodes(app,canvas)
    #drawOtherGrid(app,canvas)

    return

runApp(width=800,height=600)
