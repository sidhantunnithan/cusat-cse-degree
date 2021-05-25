from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-500.0,500.0,-250.0,250.0)

def draw_body(theta):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0,1,1)
    arm_length = 70
    xend = arm_length * math.sin(-theta * math.pi / 180)
    yend = arm_length * math.cos(-theta * math.pi / 180)
    glBegin(GL_LINES)
    glVertex2f(spineX, spineYBegin - 10)
    glVertex2f(spineX-xend, spineYBegin - 10 - yend)
    glEnd()

    glColor3f(0,1,1)
    leg_length = 70
    xend = leg_length * math.sin(theta * math.pi / 180)
    yend = leg_length * math.cos(theta * math.pi / 180)
    glBegin(GL_LINES)
    glVertex2f(spineX, spineYEnd + 10)
    glVertex2f(spineX-xend, spineYEnd + 10 - yend)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 1, 0)
    glVertex2f(spineX - 10, spineYBegin)
    glVertex2f(spineX + 10, spineYBegin)
    glVertex2f(spineX + 10, spineYEnd)
    glVertex2f(spineX - 10, spineYEnd)
    glEnd()

    x_face = spineX
    y_face = spineYBegin + 28
    r_face = 30
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    face_triangles = 31
    glVertex2f(x_face, y_face)
    for i in range (0, face_triangles + 1):
        glVertex2f(x_face + (r_face * math.cos(i *  math.pi * 2 / face_triangles)), y_face + (r_face * math.sin(i * math.pi * 2 / face_triangles)))
    glEnd()


    if(switch):
        x_eye = x_face - 20
        y_eye = y_face - 2
    else:
        x_eye = x_face + 20
        y_eye = y_face + 2
    r_eye = 5
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0, 0, 0)
    eye_triangles = 31
    glVertex2f(x_eye, y_eye)
    for i in range (0, eye_triangles + 1):
        glVertex2f(x_eye + (r_eye * math.cos(i *  math.pi * 2 / eye_triangles)), y_eye + (r_eye * math.sin(i * math.pi * 2 / eye_triangles)))
    glEnd()

    glColor3f(0,1,1)
    arm_length = 70
    xend = arm_length * math.sin(theta * math.pi / 180)
    yend = arm_length * math.cos(theta * math.pi / 180)
    glBegin(GL_LINES)
    glVertex2f(spineX, spineYBegin - 10)
    glVertex2f(spineX-xend, spineYBegin - 10 - yend)
    glEnd()

    glColor3f(0,1,1)
    leg_length = 70
    xend = leg_length * math.sin(-theta * math.pi / 180)
    yend = leg_length * math.cos(-theta * math.pi / 180)
    glBegin(GL_LINES)
    glVertex2f(spineX, spineYEnd + 10)
    glVertex2f(spineX-xend, spineYEnd + 10 - yend)
    glEnd()
    glFlush()

def initiate_drawing():
    global spineX
    spineX = -450
    global spineYBegin
    spineYBegin = 100
    global spineYEnd
    spineYEnd = 0
    global switch
    switch = False

    glLineWidth(3.0)
    glPointSize(50);   
    time = 0
    theta = 50

    while True:
        theta_new = theta * math.sin(time)
        draw_body(theta_new)
        time += 0.0009
        
        if(switch):
            spineX = spineX - 0.030
        else:
            spineX = spineX + 0.030

        if spineX > 450 or spineX < -450:
            switch = not switch

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    initiate_drawing()
    glFlush()

def main():

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Walking Man")
    init()
    glutDisplayFunc(lambda: display())
    glutMainLoop()

if __name__ == '__main__':
    main()
