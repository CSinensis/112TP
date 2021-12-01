from createCustom import *

def intersectsExistingNode(app,x,y):
    for node in app.nodes:
        distance = ((node.x - x)**2 + (node.y - y)**2)**(1/2)
        if distance <= 2*node.r/45:
            return node
    return None

def normalize(app,x,y):
    newX = (x - (app.screenMargin + app.gM))/app.bW
    newY = (y - (1/4*(app.height-2*app.screenMargin) - app.screenMargin + app.gM))/app.bH
    return newX,newY
    
def img_mousePressed(app,event):
    if inBounds(app,event.x,event.y):
        x,y = normalize(app,event.x,event.y)
        check = intersectsExistingNode(app,x,y)
        if check != None:
            if app.setStart == True or app.setEnd == True:
                setEdgeNodes(app,check)
            elif app.edgeMode != True:
                app.edgeMode = True
                app.prevNode = check
            else:
                addEdgeToGraph(app,check)
        else:
            addToGraphGridless(app,x,y)
    elif inCustomBounds(app,event.x,event.y):
        app.mode = 'BFS'
        if app.customGraph.graph != dict() and app.customGraph.end == None:
            app.customGraph.end = app.nodes[-1]
        app.gMode = 'custom'
        reset(app)
    elif inResetBounds(app,event.x,event.y):
        resetCustom(app)
    elif inHomeBounds(app,event.x,event.y):
        app.mode = 'ss'
        splashStarted(app)
    else:
        toggleCustom(app,event.x,event.y)

def addToGraphGridless(app,x,y):
    newNode = Node(x,y,f'{len(app.nodes)}')
    app.nodes.append(newNode)
    if app.customGraph.start == None:
        app.customGraph.start = app.nodes[0]
    if app.edgeMode:
        app.edgeMode = False
        newEdge = Edge(newNode,app.prevNode)
        app.edges.append(newEdge)
        app.customGraph.addEdge(newNode,app.prevNode,h(newNode,app.prevNode))

# def img_keyPressed(app,event):
#     if event.key == 'u':
#         app.customGraph.img = app.getUserInput('Enter URL for image:')
#         app.image1 = app.loadImage(app.customGraph.img)
#         app.image2 = app.image1.resize((int(790*3/4),int(590*3/4)),Image.BICUBIC)

def img_redrawAll(app,canvas):
    drawAll(app,canvas)
    drawImage(app,canvas)
    drawEdges(app,canvas)
    drawNodes(app,canvas)
    drawCustomGraphParams(app,canvas)
    drawCustomButtons(app,canvas)
    drawCustomQText(app,canvas)