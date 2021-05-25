from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 100, 0, 100)
def lineBres():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    m = 2 * (y2 - y1)
    pk = m- (x2 - x1)
    y=y1
    for x in range(int(x1),int(x2+1)):
        glVertex2f(x,y)
        pk = pk + m
        if (pk>= 0):
            y=y+1
            pk =pk- 2 * (x2 - x1)
    glEnd()
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutInitWindowPosition(50,50)
glutCreateWindow("Bresenham")
x1=float(input('x1: '))
y1=float(input('y1: '))
x2=float(input('x2: '))
y2=float(input('y2: '))
glutDisplayFunc(lineBres)
init()
glutMainLoop()