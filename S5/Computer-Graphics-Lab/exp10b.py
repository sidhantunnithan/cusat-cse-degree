from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-500.0,500.0,-250.0,250.0)

def draw_everything(theta, xball):
    glClear(GL_COLOR_BUFFER_BIT)

    yend = math.tan(theta * math.pi / 180) * 1000
    glBegin(GL_LINES)
    glVertex2f(-500, 0)
    glVertex2f(500, -yend)
    glEnd()

    yball = math.tan(theta * math.pi / 180) * (xball + 500)

    glEnable(GL_POINT_SMOOTH)
    glPointSize(1000.0)
    glBegin(GL_POINTS)
    glVertex2f(xball, -yball + 11)
    glEnd()

    glFlush()

def initiate_drawing(theta):
    glLineWidth(2.0)

    xball = -495
    draw_everything(theta, xball)

    fact = 0.0001
    while xball < 490:
        draw_everything(theta, xball)
        xball = xball + fact
        fact = fact + 0.0001

def display(theta):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    initiate_drawing(theta)
    glFlush()

def main():

    angle = int(input("Enter angle of inclination (Max - 14): "))
    if angle > 14:
        angle = 14
    elif angle < 0:
        angle = 0

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Rolling Ball")
    init()
    glutDisplayFunc(lambda: display(angle))
    glutMainLoop()

if __name__ == '__main__':
    main()
