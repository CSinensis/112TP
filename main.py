from cmu_112_graphics import *
from graphClass import *
from visualizeDijkstra import *
from visualizeBFS import *
from visualizeAStar import *
from createCustom import *
from splashscreen import *
from createCustomImg import *
from help import *
from gallery import *

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
    G1 = getHardcoded1()
    G2 = getHardcoded2()
    app.mode = 'ss'
    app.timerDelay = 500
    app.screenMargin,app.gridWidth,app.gridHeight = getScreenParams(app)
    app.gR,app.gC,app.bH,app.bW,app.gM = getGridParams(app)
    print(app.bH,app.bW)
    app.gMode = 'HC1'
    app.savedGraphs = [G1,G2]
    splashStarted(app)
    # galStarted(app)
    # reset(app)
    # resetCustom(app)

def main():
    runApp(width=800,height=600)

if (__name__ == '__main__'):
    main()


'''
Things to Fix:
- Deleting items from gallery
- help screens

DONE:
- Non-connected graphs 
- Queue needs to not immediately pop the last term 
- Be able to exit custom mode w/out crashing with blank graph 
- Make Queue clearer 
- Make weights based on manhattan distance + factor 
- fix dijk so that it ends on first instance of seen 
- Add option to choose start and end node 
'''