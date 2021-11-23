from cmu_112_graphics import *
from graphClass import *
from visualizeDijkstra import *
from visualizeBFS import *
from createCustom import *
from splashscreen import *

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
    app.mode = 'ss'
    app.screenMargin,app.gridWidth,app.gridHeight = getScreenParams(app)
    app.gR,app.gC,app.bH,app.bW,app.gM = getGridParams(app)
    app.gMode = 'HC1'
    splashStarted(app)
    # reset(app)
    # resetCustom(app)

runApp(width=800,height=600)