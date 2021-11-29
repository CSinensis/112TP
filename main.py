from cmu_112_graphics import *
from graphClass import *
from visualizeDijkstra import *
from visualizeBFS import *
from visualizeAStar import *
from createCustom import *
from splashscreen import *
from help import *

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

def main():
    runApp(width=800,height=600)

if (__name__ == '__main__'):
    main()


'''
Things to Fix:
- Queue needs to not immediately pop the last term
- Be able to exit custom mode w/out crashing with blank graph
- Non-connected graphs
- Make Queue clearer
- Make weights based on manhattan distance + factor
- fix dijk so that it ends on first instance of seen
'''