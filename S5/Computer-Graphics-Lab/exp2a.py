from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,100,0,100)

def lineDDA():
    glClear(GL_COLOR_BUFFER_BIT)
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x,y=x1,y1
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    steps=dx if dx>dy else dy
    xincrement=float(dx)/float(steps)
    yincrement=float(dy)/float(steps)
    glVertex2f(round(x),round(y))
    for k in range(int(steps)):
        x+=xincrement
        y+=yincrement
        glVertex2f(round(x),round(y))
    glEnd()
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(50,50)
glutCreateWindow("DDA")
x1=float(input('x1 coordinate:'))
y1=float(input('y1 coordinate:'))
x2=float(input('x2 coordinate:'))
y2=float(input('y2 coordinate:'))
glutDisplayFunc(lambda: lineDDA())
init()
glutMainLoop()