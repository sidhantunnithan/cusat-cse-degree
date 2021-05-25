from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def ROUND(a):
	return int(a+0.4)

def drawTriangle(x1,y1,x2,y2,x3,y3):
	glPointSize(5.0)
	glBegin(GL_TRIANGLES)
	glVertex2i(x1,y1)
	glVertex2i(x2,y2)
	glVertex2i(x3,y3)
	glEnd()
	glFlush()
    
def translation(x1,y1,x2,y2,x3,y3):
    print('Enter units to be transalated by')
    newx = int(input('x : '))
    newy = int(input('y : '))
    drawTriangle(x1 + newx,y1 + newy,x2 + newx,y2 + newy,x3 + newx,y3 + newy)


def rotation(x1,y1,x2,y2,x3,y3):
    theta = int(input('Enter the angle in degrees to be rotated w.r.t origin: '))
    theta = (theta*math.pi)/180
    newx1 = x1*math.cos(theta) - y1*math.sin(theta)
    newy1 = x1*math.sin(theta) + y1*math.cos(theta)
    newx2 = x2*math.cos(theta) - y2*math.sin(theta)
    newy2 = x2*math.sin(theta) + y2*math.cos(theta)
    newx3 = x3*math.cos(theta) - y3*math.sin(theta)
    newy3 = x3*math.sin(theta) + y3*math.cos(theta)
    drawTriangle(ROUND(newx1),ROUND(newy1),ROUND(newx2),ROUND(newy2),ROUND(newx3),ROUND(newy3))

def scaling(x1,y1,x2,y2,x3,y3):
    scale = int(input('Enter the scaling factor: '))
    drawTriangle(x1, y1, x2 * scale, y2 * scale, x3 * scale, y3 * scale)
    glColor3f(255.0,0.0,0.0)
    drawTriangle(x1,y1,x2,y2,x3,y3)

def reflection(x1,y1,x2,y2,x3,y3):
    while True:
        option = int(input('Select 1 for reflection about x axis and 2 for reflection about y axis'))
        if(option > 0 and option < 3):
            break
        else:
            print("Invalid Option")

    if option == 1:
        drawTriangle(x1,-y1,x2,-y2,x3,-y3)
    else:
        drawTriangle(-x1,y1,-x2,y2,-x3,y3)

def display():
    print('Enter the co-ordinates of the vertices of triangle: ')
    x1 = int(input('x1 : '))
    y1 = int(input('y1 : '))
    x2 = int(input('x2 : '))
    y2 = int(input('y2 : '))
    x3 = int(input('x3 : '))
    y3 = int(input('y3 : '))

    glColor3f(255.0,0.0,0.0)
    drawTriangle(x1,y1,x2,y2,x3,y3)
    glColor3f(0.0,255.0,255.0)

    while True:
        option = int(input('Enter 1 for Translation, 2 for Rotation, 3 for Scaling and 4 for Reflection: '))
        if(option < 5 and option > 0):
            break
        else:
            print("Invalid Option")

    if option == 1:
        translation(x1,y1,x2,y2,x3,y3)
    elif option == 2:
        rotation(x1,y1,x2,y2,x3,y3)
    elif option == 3:
        scaling(x1,y1,x2,y2,x3,y3)
    else:
        reflection(x1,y1,x2,y2,x3,y3)

def main():    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('2D transformations')
    glutDisplayFunc(lambda: display())
    init()
    glutMainLoop()

main()