from cmu_112_graphics import *
from visualizeHelper import *

def galStarted(app):
    app.galM = 2*app.screenMargin
    app.bannerH = (app.height - 2*app.screenMargin)/5 
    app.screenW = app.width - 2*app.screenMargin
    app.screenH = (app.height - 2*app.screenMargin) - app.bannerH
    app.galW = (app.screenW - 4*app.galM)/6
    app.galH = (app.screenH - 3*app.galM)/4
    app.bounds = getGalBounds(app)
    app.miniW = app.galW/5
    app.miniH = (app.galH - 20)/5
    return

def getGraphParams(graph):
    nodes = list(graph)
    edges = []
    seen = set()
    for node in graph:
        for neighbor in graph[node]:
            if neighbor not in seen:
                newEdge = Edge(node,neighbor)
                newEdge.weight = graph[node][neighbor]
                edges.append(newEdge)
        seen.add(node)
    return(nodes,edges)

def gal_mousePressed(app,event):
    index = inBounds(app,event.x,event.y)
    if index != None:
        app.mode = 'BFS'
        app.graph = app.savedGraphs[index]
        reset(app)


def gal_timerFired(app):
    return

def drawBackground(app,canvas):
    canvas.create_rectangle(app.screenMargin,app.screenMargin,
    app.width-app.screenMargin,app.height-app.screenMargin,fill=myBlue)
    canvas.create_rectangle(app.screenMargin,app.screenMargin,
    app.width-app.screenMargin,app.screenMargin + app.bannerH,fill=myGreen)
    canvas.create_text(app.width/2,app.screenH/8 + app.screenMargin,text=('''Pathfinding Visualizer
    Saved Graphs'''), font="Arial 50 bold",justify='center')

# def test(app,canvas):
#     canvas.create_rectangle(app.screenMargin,app.bannerH+app.screenMargin,app.screenMargin+app.screenW,app.bannerH+app.screenMargin+app.screenH,outline='pink')
#     for i in range(3):
#         for j in range(2):
#             cx,cy = app.screenW/3*(i) + app.screenW/6 + app.screenMargin,app.screenH/2*(j) + app.screenH/4 + app.bannerH + app.screenMargin
#             canvas.create_line(cx,0,cx,app.height,fill='pink')
#             canvas.create_line(0,cy,app.width,cy,fill='pink')
def inBounds(app,x,y):
    for index in range(len(app.savedGraphs)):
        startW,startH,endW,endH = app.bounds[index]
        if ((startW <= x <= endW) and (startH <= y <= endH)):
            return index
    return None

def getGalBounds(app):
    bounds = dict()
    index = 0
    for i in range(2):
        for j in range(3):
            cx,cy = app.screenMargin + app.galM + app.galW + (j)*(2*app.galW+app.galM),app.screenMargin + app.galM + app.galH + (i)*(2*app.galH+app.galM) + app.bannerH
            bounds[index] = (cx-app.galW,cy-app.galH,cx+app.galW,cy+app.galH)
            index += 1
    return bounds

def drawGal(app,canvas):
    for i in range(2):
        for j in range(3):
            cx,cy = app.screenMargin + app.galM + app.galW + (j)*(2*app.galW+app.galM),app.screenMargin + app.galM + app.galH + (i)*(2*app.galH+app.galM) + app.bannerH
            canvas.create_rectangle(cx-app.galW,cy-app.galH,cx+app.galW,cy+app.galH,fill='white')

def drawGraphs(app,canvas):
    for i in range (len(app.savedGraphs)):
        nodes,edges = getGraphParams(app.savedGraphs[i].graph)
        drawEdges(app,canvas,i,edges)
        drawNodes(app,canvas,i,nodes)

def gridToCoord(app,x,y,index):
    coordX = x*app.miniW + app.bounds[index][0]
    coordY = y*app.miniH + app.bounds[index][1]
    return (coordX,coordY)

def drawEdges(app,canvas,index,edges):
    for edge in edges:
        n1,n2 = edge.path
        x1,y1 = gridToCoord(app,n1.x,n1.y,index)
        x2,y2 = gridToCoord(app,n2.x,n2.y,index)
        canvas.create_line(x1,y1,x2,y2,fill=edge.color)

def drawNodes(app,canvas,index,nodes):
    for node in nodes:
        cx,cy = gridToCoord(app,node.x,node.y,index)
        r = node.r/2
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=node.color)
        canvas.create_text(cx,cy,text=f'{node.label}',font='Arial 10')

def gal_redrawAll(app,canvas):
    drawBackground(app,canvas)
    drawGal(app,canvas)
    drawGraphs(app,canvas)
    # test(app,canvas)

    return

