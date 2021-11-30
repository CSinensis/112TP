from cmu_112_graphics import *
from visualizeHelper import *

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
        if inDeleteBounds(app,event.x,event.y,index):
            app.savedGraphs.pop(index)
        elif inEditBounds(app,event.x,event.y,index):
            app.mode = 'create'
            resetCustom(app)
            app.customGraph = app.savedGraphs[index]
            setParams(app)
        else:
            app.mode = 'BFS'
            app.gMode = 'custom'
            app.customGraph = app.savedGraphs[index]
            reset(app)
    elif inHomeBounds(app,event.x,event.y):
        app.mode = 'ss'
        splashStarted(app)

def setParams(app):
    app.nodes = list(app.customGraph.graph)
    seen = set()
    for node in app.customGraph.graph:
        app.grid[node.x][node.y] = node
        for neighbor in app.customGraph.graph[node]:
            if neighbor not in seen:
                newEdge = Edge(node,neighbor)
                newEdge.weight = app.customGraph.graph[node][neighbor]
                app.edges.append(newEdge)
        seen.add(node)
    print(app.grid)

def drawBackground(app,canvas):
    canvas.create_rectangle(app.screenMargin,app.screenMargin,
    app.width-app.screenMargin,app.height-app.screenMargin,fill=myBlue,width=0)
    canvas.create_rectangle(app.screenMargin,app.screenMargin,
    app.width-app.screenMargin,app.screenMargin + app.bannerH,fill=myGreen,width=0)
    canvas.create_text(app.width/2,app.screenH/8 + app.screenMargin,text=('''Pathfinding Visualizer
    Saved Graphs'''), font="Arial 50 bold",justify='center')

def inBounds(app,x,y):
    for index in range(len(app.savedGraphs)):
        startW,startH,endW,endH = app.bounds[index]
        if ((startW <= x <= endW) and (startH <= y <= endH)):
            return index
    return None

def inDeleteBounds(app,x,y,index):
    i = index//3
    j = index%3
    cx = app.screenMargin + app.galW + app.galM + (j)*(2*app.galW+app.galM)
    cy = app.screenMargin + app.galH + app.galM + (i)*(2*app.galH+app.galM) + app.bannerH
    startW,startH,endW,endH = cx,cy+app.galH-2*app.menuH,cx+app.galW,cy+app.galH
    if ((startW <= x <= endW) and (startH <= y <= endH)):
        return True
    return False

def inEditBounds(app,x,y,index):
    i = index//3
    j = index%3
    cx = app.screenMargin + app.galW + app.galM + (j)*(2*app.galW+app.galM)
    cy = app.screenMargin + app.galH + app.galM + (i)*(2*app.galH+app.galM) + app.bannerH
    startW,startH,endW,endH = cx-app.galW,cy+app.galH-2*app.menuH,cx,cy+app.galH
    if ((startW <= x <= endW) and (startH <= y <= endH)):
        return True
    return False

def drawGal(app,canvas):
    for i in range(2):
        for j in range(3):
            cx = app.screenMargin + app.galW + app.galM + (j)*(2*app.galW+app.galM)
            cy = app.screenMargin + app.galH + app.galM + (i)*(2*app.galH+app.galM) + app.bannerH
            canvas.create_rectangle(cx-app.galW,cy-app.galH,cx+app.galW,cy+app.galH,fill='white')
            canvas.create_rectangle(cx-app.galW,cy+app.galH-2*app.menuH,cx,cy+app.galH,fill=myYellow)
            canvas.create_text((2*cx-app.galW)/2,cy+app.galH-app.menuH,text='Edit',font = 'Arial 20')
            canvas.create_rectangle(cx,cy+app.galH-2*app.menuH,cx+app.galW,cy+app.galH,fill='red3')
            canvas.create_text((2*cx+app.galW)/2,cy+app.galH-app.menuH,text='Delete',font = 'Arial 20')

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
        canvas.create_text(cx,cy,text=f'{node.label}',font='Arial 9')

def gal_redrawAll(app,canvas):
    drawBackground(app,canvas)
    drawGal(app,canvas)
    drawGraphs(app,canvas)
    drawHome(app,canvas)