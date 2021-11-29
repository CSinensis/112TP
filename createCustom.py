from cmu_112_graphics import *
from graphClass import *
from dijkstra import *
from visualizeHelper import *
import random

def create_mousePressed(app,event):
    if inBounds(app,event.x,event.y):
        col = int((event.x - app.screenMargin + app.bW/2)/app.bW)
        row = int((event.y - 1/4*(app.height-2*app.screenMargin) + app.screenMargin + app.bH/2)/app.bH)
        if app.grid[col][row] != None:
            if app.edgeMode != True:
                app.edgeMode = True
                app.prevNode = app.grid[col][row]
            else:
                app.edgeMode = False
                newEdge = Edge(app.grid[col][row],app.prevNode)
                app.edges.append(newEdge)
                app.customGraph.addEdge(app.grid[col][row],app.prevNode,random.randrange(1,10))
        else:
            newNode = Node(col,row,f'{len(app.nodes)}')
            app.nodes.append(newNode)
            app.grid[col][row] = newNode
            if app.edgeMode != True:
                app.edgeMode = True
                app.prevNode = newNode
            else:
                app.edgeMode = False
                newEdge = Edge(newNode,app.prevNode)
                app.edges.append(newEdge)
                app.customGraph.addEdge(newNode,app.prevNode,random.randrange(1,10))
    elif inCustomBounds(app,event.x,event.y):
        app.mode = 'BFS'
        app.startNode,app.endNode = app.nodes[0],app.nodes[-1]
        app.gMode = 'custom'
        reset(app)

def create_keyPressed(app,event):
    if event.key == 's':
        app.savedGraphs.append(copy.deepcopy(app.customGraph))
    

def drawEdges(app,canvas):
    for edge in app.edges:
        n1,n2 = edge.path
        x1,y1 = gridToCoord(app,n1.x,n1.y)
        x2,y2 = gridToCoord(app,n2.x,n2.y)
        avgX,avgY = (x1+x2)/2,(y1+y2)/2
        canvas.create_line(x1,y1,x2,y2,fill=edge.color)

def drawNodes(app,canvas):
    for node in app.nodes:
        cx,cy = gridToCoord(app,node.x,node.y)
        r = node.r
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=node.color)
        canvas.create_text(cx,cy,text=f'{node.label}')

def create_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)