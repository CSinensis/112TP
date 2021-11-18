from cmu_112_graphics import *

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

def drawGrid(app,canvas):
    width = app.bW
    height = app.bH
    margin = app.gM
    gridStartHeight = app.screenMargin + 1/4*(app.height-2*app.screenMargin)
    gridStartWidth = app.screenMargin
    print(gridStartHeight,gridStartWidth)
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

# 5 + 152.5 + app.gridHeight/app.Rows * 100
# 157.5 + 442.5/10 * 11
def redrawAll(app,canvas):
    drawGrid(app,canvas)
    return

runApp(width=800,height=600)
