from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import math

WHITE = [1, 1, 1]
RED = [1, 0, 0]

isOpen = False

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(0, 500, 0, 500)

def plotPixel(x, y, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def midPointLine(x1, x2, y1, y2, color):
    if(x1 < x2 and y1 < y2):
        dx = x2 - x1
        dy = y2 - y1
        d = dy - dx/2
        x, y = x1, y1
        
        plotPixel(x, y, color)

        while(x < x2):
            x += 1
            if d < 0:
                d += dy
            else:
                d += (dy - dx)
                y += 1
            plotPixel(x, y, color)

    elif(x1 < x2 and y1 > y2):
        dx = x2 - x1
        dy = y1 - y2
        d = dy - dx/2
        x, y = x1, y1
        
        plotPixel(x, y, color)

        while(x < x2):
            x += 1
            if d < 0:
                d += dy
            else:
                d += (dy - dx)
                y -= 1
            plotPixel(x, y, color)

    elif(x1 == x2):
        y = y1
        plotPixel(x1, y, color)
        while(y < y2):
            y += 1
            plotPixel(x1, y, color)
    
    else:
        x = x1
        plotPixel(x, y1, color)
        while(x < x2):
            x += 1
            plotPixel(x, y1, color)

def buildHouse():

    glClear(GL_COLOR_BUFFER_BIT)

    # Wall
    midPointLine(150, 350, 100, 100, WHITE)
    midPointLine(150, 150, 100, 300, WHITE)
    midPointLine(350, 350, 100, 300, WHITE)
    midPointLine(150, 350, 300, 300, WHITE)

    # Roof
    midPointLine(150, 250, 300, 400, WHITE)
    midPointLine(250, 350, 400, 300, WHITE)

    # Door
    midPointLine(200, 200, 100, 250, WHITE)
    midPointLine(300, 300, 100, 250, WHITE)
    midPointLine(200, 300, 250, 250, WHITE)

    if(isOpen):

        # Door
        midPointLine(270, 300, 200, 250, WHITE)
        midPointLine(270, 270, 150, 200, WHITE)
        midPointLine(270, 300, 150, 100, WHITE)

        # Door Knob
        glBegin(GL_TRIANGLE_FAN)
        triangles = 31
        xend, yend = 275, 320
        glVertex2f(xend, 500-yend)
        for i in range (0, triangles + 1):
            glVertex2f(xend + (2 * math.cos(i *  math.pi * 2 / triangles)), 500 - yend + (2 * math.sin(i * math.pi * 2 / triangles)))
        glEnd()

        # Floor
        midPointLine(200, 274, 145, 145, RED)
    else:

        # Door Knob
        glBegin(GL_TRIANGLE_FAN)
        triangles = 31
        xend, yend = 220, 320
        glVertex2f(xend, 500-yend)
        for i in range (0, triangles + 1):
            glVertex2f(xend + (5 * math.cos(i *  math.pi * 2 / triangles)), 500 - yend + (5 * math.sin(i * math.pi * 2 / triangles)))
        glEnd()

def mouse(btn, state, x, y):
    global isOpen
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        isOpen = False
        buildHouse()
    elif btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        isOpen = True
        buildHouse()
    glFlush()

def display():
    buildHouse()
    glFlush()

def main():

    print("Left Click to Open Door, Right Click to Close Door")

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow(b"Door Open/Close")
    init()
    glutDisplayFunc(lambda: display())
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ == "__main__":
    main()