from cmu_112_graphics import *
from graphClass import *

def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

myBlue = rgbString(0, 159, 183)
myYellow = rgbString(254, 215, 102)
myGreen = rgbString(104, 163, 87)
myRed = rgbString(109, 33, 60)

def customImgStarted(app):
    app.image = app.loadImage(app.customGraph.url)
    app.customGraph.imgMode = True
    app.customGraph.img = app.image.resize((int(790*3/4),int(590*3/4)),Image.BICUBIC)

def resetCustom(app):
    app.customGraph = Graph(dict())
    app.grid = [[None]*app.gC for row in range(app.gR)]
    app.edgeMode = False
    app.prevNode = None
    app.nodes = []
    app.edges = []
    app.setStart = False
    app.setEnd = False
    app.Q = []
    app.customQText = ''
    app.customMessage = '''Click here to exit 
    editing mode'''

def reset(app):
    if app.gMode == 'HC1':
        app.G = getHardcoded1()
        print("YE",app.G.start,app.G.end)
    elif app.gMode == 'HC2':
        app.G = getHardcoded3()
    elif app.gMode == 'custom':
        app.G = copy.deepcopy(app.customGraph)
        print(app.G.graph)
        print("YE",app.G.start,app.G.end)
    app.grid = [[None]*app.gC for row in range(app.gR)]
    app.nodes = []
    app.edges = []
    app.step = 0
    app.cache = None
    app.solution = None
    app.Q = []
    app.auto = False
    app.customMessage = ('''Click here to create
    a custom graph''')
    setGraph(app)

def galStarted(app):
    app.galM = 2*app.screenMargin
    app.menuH = 20
    app.bannerH = (app.height - 2*app.screenMargin)/5 
    app.screenW = app.width - 2*app.screenMargin
    app.screenH = (app.height - 2*app.screenMargin) - app.bannerH
    app.galW = (app.screenW - 4*app.galM)/6
    app.galH = (app.screenH - 3*app.galM)/4
    app.bounds = getGalBounds(app)
    app.miniW = app.galW/5
    app.miniH = (app.galH - app.menuH)/5
    return

def splashStarted(app):
    app.sMargin = 100
    app.optStartW,app.optStartH = app.sMargin,3*app.height/4 - 50 + app.screenMargin
    app.optEndW,app.optEndH = app.width-app.sMargin,3*app.height/4 + 50 + app.screenMargin
    app.optBoxW = (app.optEndW-app.optStartW-2*app.screenMargin)/3

def getGalBounds(app):
    bounds = dict()
    index = 0
    for i in range(2):
        for j in range(3):
            cx,cy = app.screenMargin + app.galM + app.galW + (j)*(2*app.galW+app.galM),app.screenMargin + app.galM + app.galH + (i)*(2*app.galH+app.galM) + app.bannerH
            bounds[index] = (cx-app.galW,cy-app.galH,cx+app.galW,cy+app.galH)
            index += 1
    return bounds

def getHardcoded1():
    A = Node(4,2,'A')
    B = Node(3,4,'B')
    C = Node(5,4,'C')
    D = Node(7,4,'D')
    E = Node(4,6,'E')
    F = Node(6,6,'F')
    G = Node(7,8,'G')
    H = Node(3,7,'H')
    testGraph = {
        A:{B:2,C:4,D:3},
        B:{A:2,H:10},
        C:{A:4,E:5,F:2},
        D:{A:3,F:8},
        E:{C:5,H:6},
        F:{D:8,C:5,G:3},
        G:{F:3},
        H:{E:6,B:10}
    }
    G = Graph(testGraph)
    G.start = A
    G.end = H
    print("NE",G.start,G.end)
    return G

def getHardcoded2():
    A = Node(4,2,'A')
    B = Node(3,4,'B')
    C = Node(5,4,'C')
    D = Node(7,4,'D')
    E = Node(4,6,'E')
    F = Node(6,6,'F')
    testGraph = {
        A:{B:2,C:4,D:3},
        B:{A:2},
        C:{A:4,E:5,F:2},
        D:{A:3,F:8},
        E:{C:5},
        F:{D:8,C:5}
    }
    G = Graph(testGraph)
    G.start = A
    G.end = F
    return G

def getHardcoded3():
    X = Node(5,1,'X')
    A = Node(2,3,'A')
    B = Node(4,3,'B')
    C = Node(7,3,'C')
    D = Node(2,5,'D')
    E = Node(8,1,'E')
    F = Node(2,7,'F')
    G = Node(4,7,'G')
    H = Node(4,5,'H')
    I = Node(7,6,'I')
    J = Node(9,6,'J')
    K = Node(6,8,'K')
    L = Node(8,4,'L')
    Y = Node(5,9,'Y')
    largerTestGraph = {
    X:{E:4,A:7,B:3,C:5},
    A:{X:7,B:3,D:4},
    B:{X:3,A:3,D:4,H:2},
    C:{X:5,L:2},
    D:{A:4,B:4,F:2},
    E:{X:4},
    F:{D:2,H:5},
    G:{H:2,Y:4},
    H:{G:2,B:2,F:5},
    I:{L:4,J:6,K:4},
    J:{L:7,I:6},
    K:{I:4,Y:5},
    L:{C:2,I:4,J:7},
    Y:{G:4,K:5}}
    G = Graph(largerTestGraph)
    G.start = X
    G.end = Y
    return G
    
def setGraph(app):
    app.nodes = list(app.G.graph)
    seen = set()
    for node in app.G.graph:
        for neighbor in app.G.graph[node]:
            if neighbor not in seen:
                newEdge = Edge(node,neighbor)
                newEdge.weight = app.G.graph[node][neighbor]
                app.edges.append(newEdge)
        seen.add(node)