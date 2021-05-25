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
    glutCreateWindow("Clipping Algorithms")
    init()

def drawClippingWindow(xClip1, xClip2, yClip1, yClip2):
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0]
    ]
    points = [
        [xClip1, yClip1],
        [xClip2, yClip1],
        [xClip2, yClip2],
        [xClip1, yClip2]
    ]

    glColor3f(1.0, 1.0, 1.0)
    for e in edges:
        for v in e:
            glVertex2fv(points[v])

def drawLine(x1, x2, y1, y2):
    edges = [
        [0, 1]
    ]
    points = [
        [x1, y1],
        [x2, y2]
    ]

    glColor3f(0.0, 0.0, 1.0)
    for e in edges:
        for v in e:
            glVertex2fv(points[v])


INSIDE = 0
LEFT = 1
RIGHT = 2
DOWN = 4
TOP = 8

def getParam(x, y, xClip1, xClip2, yClip1, yClip2):
    param = INSIDE

    if x < xClip1:
        param |= LEFT

    elif x > xClip2:
        param |= RIGHT

    if y < yClip1:
        param |= DOWN

    elif y > yClip2:
        param |= TOP

    return param

def cohenSutherland(x1, x2, y1, y2, xClip1, xClip2, yClip1, yClip2):
    drawLine(x1, x2, y1, y2)

    param1 = getParam(x1, y1, xClip1, xClip2, yClip1, yClip2)
    param2 = getParam(x2, y2, xClip1, xClip2, yClip1, yClip2)
    accept = False

    while True:
        if param1 == 0 and param2 == 0:
            accept = True
            break

        elif param1 & param2 != 0:
            break

        else:
            x = float()
            y = float()

            if param1 != 0:
                param_out = param1
            else:
                param_out = param2

            if param_out & TOP:
                y = yClip2
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

            elif param_out & DOWN:
                y = yClip1
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

            elif param_out & LEFT:
                x = xClip1
                y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

            elif param_out & RIGHT:
                x = xClip2
                y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

            if param_out == param1:
                x1, y1 = x, y
                param1 = getParam(x, y, xClip1, xClip2, yClip1, yClip2)

            else:
                x2, y2 = x, y
                param2 = getParam(x, y, xClip1, xClip2, yClip1, yClip2)

    if accept:
        edges = [[0, 1]]
        points = [
            [x1, y1],
            [x2, y2]
        ]
        rgb = [1.0, 0.0, 0.0]
        glColor3f(1.0, 0.0, 0.0)
        for e in edges:
            for v in e:
                glVertex2fv(points[v])

        drawClippingWindow(xClip1, xClip2, yClip1, yClip2)

    else:
        print("The given line cannot be clipped!")

def clipLine(x1, x2, y1, y2, xClip1, xClip2, yClip1, yClip2):

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    glBegin(GL_LINES)

    cohenSutherland(x1, x2, y1, y2, xClip1, xClip2, yClip1, yClip2)

    glEnd()
    glFlush()


def drawPolygons(edges, points, rgb):
    glColor3f(rgb[0], rgb[1], rgb[2])
    for e in edges:
        for v in e:
            glVertex2fv(points[v])


def getPolygon():
    n = int(input("Enter the number of edges : "))
    edges = list(list())
    points = list(list())

    for i in range(n):
        edges += [[i, (i+1) % n]]

    for i in range(n):
        x = float(input("Enter the x-coordinate value of point " + str(i+1) + ": "))
        y = float(input("Enter the y-coordinate value of point " + str(i+1) + ": "))
        points += [[x, y]]

    return edges, points


def drawGivenPolygon(edges, points):
    rgb = [0.0, 0.0, 1.0]
    drawPolygons(edges, points, rgb)


def SHC(points, xClip1, xClip2, yClip1, yClip2):
    global x_new, y_new, x_newr, y_newr, x_newb, y_newb, x_newt, y_newt
    x_new = []
    y_new = []
    x_newr = []
    y_newr = []
    x_newb = []
    y_newb = []
    x_newt = []
    y_newt = []
    n = len(points)
    for i in range(n-1):
        clipl(points[i][0], points[i][1],
              points[i+1][0], points[i+1][1], xClip1)
    clipl(points[n-1][0], points[n-1][1], points[0][0], points[0][1], xClip1)

    n = len(x_new)
    for i in range(n-1):
        clipr(x_new[i], y_new[i], x_new[i+1], y_new[i+1], xClip2)
    clipr(x_new[n-1], y_new[n-1], x_new[0], y_new[0], xClip2)

    n = len(x_newr)
    for i in range(n-1):
        clipb(x_newr[i], y_newr[i], x_newr[i+1], y_newr[i+1], yClip1)
    clipb(x_newr[n-1], y_newr[n-1], x_newr[0], y_newr[0], yClip1)

    n = len(x_newb)
    for i in range(n-1):
        clipt(x_newb[i], y_newb[i], x_newb[i+1], y_newb[i+1], yClip2)
    clipt(x_newb[n-1], y_newb[n-1], x_newb[0], y_newb[0], yClip2)

    n = len(x_newt)
    newEdges = list(list())
    for i in range(n):
        newEdges += [[i, (i+1) % n]]

    newPoints = list(list())
    for i in range(len(x_newt)):
        newPoints += [[x_newt[i], y_newt[i]]]

    glColor3f(1.0, 0.0, 0.0)
    for e in newEdges:
        for v in e:
            glVertex2fv(newPoints[v])


def clipl(x1, y1, x2, y2, xClip1):

    if x2 - x1 != 0:
        m = (y2 - y1)/(x2 - x1)
    else:
        m = 4000
    if x1 >= xClip1 and x2 >= xClip1:

        x_new.append(x2)
        y_new.append(y2)

    elif x1 < xClip1 and x2 >= xClip1:

        x_new.append(xClip1)
        y_new.append(y1 + m*(xClip1 - x1))
        x_new.append(x2)
        y_new.append(y2)

    elif x1 >= xClip1 and x2 < xClip1:

        x_new.append(xClip1)
        y_new.append(y1 + m*(xClip1 - x1))


def clipr(x1, y1, x2, y2, xClip2):
    if x2 - x1 != 0:
        m = (y2 - y1)/(x2 - x1)
    else:
        m = 4000

    if x1 <= xClip2 and x2 <= xClip2:

        x_newr.append(x2)
        y_newr.append(y2)

    elif x1 > xClip2 and x2 <= xClip2:

        x_newr.append(xClip2)
        y_newr.append(y1 + m*(xClip2 - x1))
        x_newr.append(x2)
        y_newr.append(y2)

    elif x1 <= xClip2 and x2 > xClip2:
        x_newr.append(xClip2)
        y_newr.append(y1 + m*(xClip2 - x1))


def clipt(x1, y1, x2, y2, yClip2):
    if (y2-y1) != 0:
        m = (x2-x1)/(y2-y1)
    else:
        m = 4000
    if y1 <= yClip2 and y2 <= yClip2:
        x_newt.append(x2)
        y_newt.append(y2)
    elif y1 > yClip2 and y2 <= yClip2:
        x_newt.append(x1+m*(yClip2-y1))
        y_newt.append(yClip2)
        x_newt.append(x2)
        y_newt.append(y2)

    elif y1 <= yClip2 and y2 > yClip2:
        x_newt.append(x1+m*(yClip2 - y1))
        y_newt.append(yClip2)


def clipb(x1, y1, x2, y2, yClip1):
    if (y2-y1) != 0:
        m = (x2-x1)/(y2-y1)
    else:
        m = 4000
    if y1 >= yClip1 and y2 >= yClip1:
        x_newb.append(x2)
        y_newb.append(y2)
    elif y1 < yClip1 and y2 >= yClip1:
        x_newb.append(x1+m*(yClip1-y1))
        y_newb.append(yClip1)
        x_newb.append(x2)
        y_newb.append(y2)

    elif y1 >= yClip1 and y2 < yClip1:
        x_newb.append(x1+m*(yClip1 - y1))
        y_newb.append(yClip1)

def clipPolygon(edges, points, xClip1, xClip2, yClip1, yClip2):

    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    glBegin(GL_LINES)

    drawClippingWindow(xClip1, xClip2, yClip1, yClip2)

    glColor3f(0.0, 0.0, 0.1)
    for e in edges:
        for v in e:
            glVertex2fv(points[v])

    SHC(points, xClip1, xClip2, yClip1, yClip2)

    glEnd()
    glFlush()

def main():
    print("Enter 1 to clip a line using Cohen Sutherland Line Clipping algorithm")
    print("Enter 2 to clip a polygon using Sutherland Hodgeman polygon clipping algorithm")
    ch = 0

    while True:
        ch = int(input("Enter your choice : "))
        if ch!=1 and ch!=2:
            print("Invalid choice.")
        else:
            break

    print("Enter the clipping window size : ")
    xClip1 = float(input("Enter the minimum window value of x : "))
    xClip2 = float(input("Enter the maximum window value of x : "))
    yClip1 = float(input("Enter the minimum window value of y : "))
    yClip2 = float(input("Enter the maximum window value of y : "))

    if ch == 1:
        x1 = float(input("Enter the initial x coordinate value : "))
        x2 = float(input('Enter the final x coordinate value : '))
        y1 = float(input("Enter the initial y coordinate value : "))
        y2 = float(input("Enter the final y coordinate value : "))

        glutFunct()
        glutDisplayFunc(lambda: clipLine(x1, x2, y1, y2, xClip1, xClip2, yClip1, yClip2))

    if ch == 2:
        edges, points = getPolygon()

        glutFunct()
        glutDisplayFunc(lambda: clipPolygon(edges, points, xClip1, xClip2, yClip1, yClip2))

    glutMainLoop()

if __name__ == '__main__':
    main()
