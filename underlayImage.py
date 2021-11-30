from cmu_112_graphics import *
from visualizeHelper import *
from startingParams import *
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
    app.url = None
    app.screenMargin,app.gridWidth,app.gridHeight = getScreenParams(app)
    app.gR,app.gC,app.bH,app.bW,app.gM = getGridParams(app)

# def redrawAll(app, canvas):
#     canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
#     canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))


def mousePressed(app,event):
    app.url = app.getUserInput('Enter URL for image:')
    app.image1 = app.loadImage(app.url)
    app.image2 = app.image1.resize((int(790*3/4),int(590*3/4)),Image.BICUBIC)
    return

def keyPressed(app,event):
    return

def redrawAll(app,canvas):
    startH = 1/4*(app.height-2*app.screenMargin) 
    startW = 2*app.screenMargin
    if app.url != None:
        canvas.create_image(startW + app.gridWidth/2,startH + app.gridHeight/2,image=ImageTk.PhotoImage(app.image2))
    drawGrid(app,canvas)

def main():
    runApp(width=800,height=600,)

if (__name__ == '__main__'):
    main()
