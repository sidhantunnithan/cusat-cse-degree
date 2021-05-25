from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-250.0, 250.0, -250.0, 250.0)

def glutFunct():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Bezier Curve Algorithm")
    init()

def plotPoint(x, y):
    glBegin(GL_POINTS)
    glVertex3f(x, y, 0)
    glEnd()

def getCoeff(n):
    coeff = []
    for k in range(n+1):
        coeff += [1]
        for j in range(k+1, n+1):
            coeff[k] *= j
        for j in range(1, n-k+1):
            coeff[k] /= j
    return coeff


def getBezierPoints(u, n, coeff, controlPoints):
    x, y = 0.0, 0.0
    for k in range(n):
        blendParam = coeff[k] * math.pow(u, k) * math.pow(1-u, n-1-k)
        x += controlPoints[k][0] * blendParam
        y += controlPoints[k][1] * blendParam

    return x, y  

def display(n, controlPoints, bezierPoints):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)

    coeff = getCoeff(n-1)
    for k in range(bezierPoints):
        u = float(k/bezierPoints)
        x, y = getBezierPoints(u, n, coeff, controlPoints)
        plotPoint(x, y)

    glFlush()

def main():
    n = int(input("\nEnter the number of control points : "))
    bezierPoints = int(input("Enter the number of Bezier curve points : "))
    controlPoints = list(list())
    for i in range(n):
        x = float(input("Enter the x-coordinate for control point " + str(i+1) + ": "))
        y = float(input("Enter the y-coordinate for control point " + str(i+1) + ": "))
        controlPoints += [[x, y]]

    glutFunct()
    glutDisplayFunc(lambda: display(n, controlPoints, bezierPoints))
    glutMainLoop()

if __name__ == '__main__':
    main()