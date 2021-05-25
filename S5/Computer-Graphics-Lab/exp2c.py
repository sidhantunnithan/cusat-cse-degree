from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50.0, 50.0, -50.0, 50.0)


def midPointLine(x1, x2, y1, y2):
    xs = []
    ys = []
    dx = x2 - x1
    dy = y2 - y1
    d = dy - dx/2
    x, y = x1, y1
    xs.append(x)
    ys.append(y)

    while(x < x2):
        x += 1
        if d < 0:
            d += dy
        else:
            d += (dy - dx)
            y += 1
        xs.append(x)
        ys.append(y)

    return xs, ys


def drawLine(x1, x2, y1, y2):
    xs, ys = midPointLine(x1, x2, y1, y2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    for i in range(len(xs)):
        glVertex2f(xs[i], ys[i])

    glEnd()
    glFlush()


def main():
    x1 = float(input("Enter first x-coordinate : "))
    x2 = float(input("Enter second x-coordinate : "))
    y1 = float(input("Enter first y-coordinate : "))
    y2 = float(input("Enter second y-coordinate : "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Mid-Point Line Generation")
    glutDisplayFunc(lambda: drawLine(x1, x2, y1, y2))
    init()
    glutMainLoop()


if __name__ = '__main__':
    main()
