from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

FACTOR = 0.0009

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-500.0,500.0,-250.0,250.0)

def drawPendulum(theta):

    glClear(GL_COLOR_BUFFER_BIT)

    xend = 292 * math.sin(theta * math.pi / 180)
    yend = 292 * math.cos(theta * math.pi / 180)

    glBegin(GL_LINES)
    glVertex2f(0, 250.0)
    glVertex2f(xend, 250 - yend)
    glEnd()
    
    glEnable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex2f(xend, 250 - yend)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    triangles = 31
    glVertex2f(xend, 250 - yend)
    for i in range (0, triangles + 1):
        glVertex2f(xend + (20 * math.cos(i *  math.pi * 2 / triangles)), 250 - yend + (20 * math.sin(i * math.pi * 2 / triangles)))
    glEnd()

    glFlush()

def initiate_drawing(theta):
    glLineWidth(3.0)
    time = 0

    while True:
        theta_new = theta * math.sin(time)
        drawPendulum(theta_new)
        time += FACTOR

def display(theta):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    initiate_drawing(theta)
    glFlush()

def main():

    angle = int(input("Enter maximum angle : "))

    if angle > 90:
        angle = 90
    elif angle < 0:
        angle = 0
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Swinging Pendulum")
    init()
    glutDisplayFunc(lambda: display(angle))
    glutMainLoop()

if __name__ == '__main__':
    main()
