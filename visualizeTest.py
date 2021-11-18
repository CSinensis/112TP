from cmu_112_graphics import *
from dijkstra import *
import math
class Node(object):
    def __init__(self,cx,cy,r):
        self.cx = cx
        self.cy = cy
        self.r = r

    def __repr__(self):
        return f'x:{self.cx},y:{self.cy}'


def appStarted(app):
    app.G = Graph()
    app.nodes = dict()
    app.seen = set()
    assignPos(app)
    print(app.nodes)
    return

def assignPos(app):
    for key in app.G.graph:
        if app.seen==set():
            app.seen.add(key)
            app.nodes[key] = Node(app.width/2,15,10)
        angle = (math.pi)/(len(app.G.graph[key]))
        a = 1
        for i in app.G.graph[key]:
            print(i)
            if i not in app.seen:
                dx = 50*math.cos(angle*a)
                dy = 100*math.sin(angle*a)
                if key in app.nodes:
                    prev = app.nodes[key]
                    newNode = Node(prev.cx+dx,prev.cy+dy,10)
                    app.seen.add(i)
                    app.nodes[i] = newNode
            a+=1
        print(app.seen)
        print(key)

def drawGraph(app,canvas):
    for key in app.nodes:
        i = app.nodes[key]
        canvas.create_oval(i.cx-i.r,i.cy-i.r,i.cx+i.r,i.cy+i.r,fill='cyan')
        canvas.create_text(i.cx,i.cy,text=f'{key}')

def redrawAll(app,canvas):
    drawGraph(app,canvas)
    return

runApp(width=400,height=400)

#print(app.G)