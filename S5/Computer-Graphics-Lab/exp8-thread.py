from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import threading
import inspect

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 500, 0, 500)


def plotPixel(x, y, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def boundaryFill(x, y, boundaryColor, fillcolor):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)

    if (color != boundaryColor).any() and (color != fillcolor).any():
        plotPixel(x, y, fillcolor)
        if(not(x + 1 >= 500) and (glReadPixels(x+1, y, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            boundaryFill(x+1, y, boundaryColor, fillcolor)
        if(not(x - 1 < 0) and (glReadPixels(x-1, y, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            boundaryFill(x-1, y, boundaryColor, fillcolor)
        if(not(y + 1 >= 500) and (glReadPixels(x, y+1, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            boundaryFill(x, y+1, boundaryColor, fillcolor)
        if(not(x -1 < 0) and (glReadPixels(x+1, y, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            boundaryFill(x, y-1, boundaryColor, fillcolor)


def floodFill(x, y, backgroundColor, fillcolor):

    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (color == backgroundColor).all() and (color != fillcolor).any():
        plotPixel(x, y, fillcolor)
        if(not(x + 1 >= 500) and (glReadPixels(x+1, y, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            floodFill(x+1, y, backgroundColor, fillcolor)
        if(not(x - 1 < 0) and (glReadPixels(x-1, y, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            floodFill(x-1, y, backgroundColor, fillcolor)
        if(not(y + 1 >= 500) and (glReadPixels(x, y+1, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            floodFill(x, y+1, backgroundColor, fillcolor)
        if(not(x -1 < 0) and (glReadPixels(x+1, y, 1, 1, GL_RGB, GL_FLOAT) != fillcolor).any()):
            floodFill(x, y-1, backgroundColor, fillcolor)

def mouse(btn, state, x, y):
    
    y = 500 - y
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        fillcolor = [1, 1, 1]
        boundaryColor = [1, 0, 0]
        boundaryFill(x, y, boundaryColor, fillcolor)

    elif btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        fillcolor = [0, 0.5, 0]
        backgroundColor = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
        floodFill(x, y, backgroundColor, fillcolor)


def display():
    glLineWidth(3)
    glColor3f(1, 0, 0)
    # glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_LOOP)
    glVertex2i(200, 200)
    glVertex2i(200, 300)
    glVertex2i(300, 300)
    glVertex2i(300, 200)
    glEnd()

    glFlush()


def main():
    print("Click with Left Mouse Button for flood filling desired area")
    print("Click with Right Mouse Button for boundary filling desired area")

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Seed Fill Algorithms")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()

threading.stack_size(2 ** 28-1)
thread = threading.Thread(target=main)
sys.setrecursionlimit(500000)

thread.start()
