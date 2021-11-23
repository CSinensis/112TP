from cmu_112_graphics import *
from graphClass import *
from visualizeDijkstra import *
from visualizeBFS import *


##########################################
# Help Mode
##########################################

def helpMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='This is the help screen!', font=font)
    canvas.create_text(app.width/2, 250, text='(Insert helpful message here)', font=font)
    canvas.create_text(app.width/2, 350, text='Press any key to return to the game!', font=font)

def helpMode_keyPressed(app, event):
    app.mode = 'gameMode'

##########################################
# Main App
##########################################
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
    app.mode = 'BFS'
    app.screenMargin,app.gridWidth,app.gridHeight = getScreenParams(app)
    app.gR,app.gC,app.bH,app.bW,app.gM = getGridParams(app)
    reset(app)

runApp(width=800,height=600)