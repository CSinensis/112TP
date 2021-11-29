from cmu_112_graphics import *
def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,100,100,fill='grey')
    canvas.create_rectangle(100,0,200,100,fill='green')
    canvas.create_rectangle(200,0,300,100,fill='purple')
    return

def appStarted(app):
    return

runApp(width=800,height=600)
