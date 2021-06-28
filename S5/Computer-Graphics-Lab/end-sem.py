""" 
    Sidhant Unnithan
    89 CSE-B
    Computer Graphics Lab Exam
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# constants
TRIANGLES=31

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Child with Balloons")
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-500.0,500.0,0.0,500.0)

def midptellipse(rx, ry, xc, yc):
 
    glBegin(GL_LINES)
    
    x = 0
    y = ry
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y
    while (dx < dy):
        glVertex2f(x+xc, y+yc)
        glVertex2f(-x+xc, y+yc)
        glVertex2f(x+xc, -y+yc)
        glVertex2f(-x+xc, -y+yc)

        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)
 
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry))
 
    while (y >= 0):
        glVertex2f(x+xc, y+yc)
        glVertex2f(-x+xc, y+yc)
        glVertex2f(x+xc, -y+yc)
        glVertex2f(-x+xc, -y+yc)

        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)
    
    glEnd()

def drawBalloons(offset): 
    glColor3f(1,0,0)
    midptellipse(40, 50, 70, 370+offset)
    glColor3f(0,1,0)
    midptellipse(40, 50, -20, 370+offset)
    glColor3f(0,0,1)
    midptellipse(40, 50, 160, 370+offset)

    if(offset):
        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(70, 320+offset)
        glVertex2f(70, 270+offset)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(-20, 320+offset)
        glVertex2f(-20, 270+offset)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(160, 320+offset)
        glVertex2f(160, 270+offset)
        glEnd()

    else:
        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(70, 320)
        glVertex2f(70, 270)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(-20, 320)
        glVertex2f(70, 270)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(1,1,1)
        glVertex2f(160, 320)
        glVertex2f(70, 270)
        glEnd()

def buildScene(offset):
    glClear(GL_COLOR_BUFFER_BIT)
    
    # face
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0.7, 0.4)
    TRIANGLES = 31
    x_face, y_face = 0, 200
    r_face = 40
    glVertex2f(x_face, y_face)
    for i in range (0, TRIANGLES + 1):
        glVertex2f(x_face + (r_face * math.cos(i *  math.pi * 2 / TRIANGLES)), y_face + (r_face * math.sin(i * math.pi * 2 / TRIANGLES)))
    glEnd()

    # eyes
    glColor3f(0,0,0)
    TRIANGLES = 31
    x_leftEye, y_leftEye = -20, 210
    x_rightEye, y_rightEye = 20, 210
    r_eye = 5
    
    # left eye
    glBegin(GL_TRIANGLE_FAN) 
    glVertex2f(x_leftEye, y_leftEye)
    for i in range (0, TRIANGLES + 1):
        glVertex2f(x_leftEye + (r_eye * math.cos(i *  math.pi * 2 / TRIANGLES)), y_leftEye + (r_eye * math.sin(i * math.pi * 2 / TRIANGLES)))
    glEnd()

    # right eye
    glBegin(GL_TRIANGLE_FAN) 
    glVertex2f(x_rightEye, y_rightEye)
    for i in range (0, TRIANGLES + 1):
        glVertex2f(x_rightEye + (r_eye * math.cos(i *  math.pi * 2 / TRIANGLES)), y_rightEye + (r_eye * math.sin(i * math.pi * 2 / TRIANGLES)))
    glEnd()

    # # mouth
    # glBegin(GL_TRIANGLE_FAN)
    # glColor3f(0, 0, 0)
    # TRIANGLES = 31
    # x_mouth, y_mouth = 0, 190
    # r_mouth = 10
    # glVertex2f(x_mouth, y_mouth)
    # for i in range (0, TRIANGLES + 1):
    #     glVertex2f(x_mouth + (r_mouth * math.cos(i *  math.pi * 2 / TRIANGLES)), y_mouth + (r_mouth * math.sin(i * math.pi * 2 / TRIANGLES)))
    # glEnd()

    # # emotion
    # if(offset):
    #     glBegin(GL_POLYGON)
    #     glColor3f(1, 0.7, 0.4)
    #     glVertex2f(-10, 180)
    #     glVertex2f(10, 180)
    #     glVertex2f(10, 190)
    #     glVertex2f(-10, 190)
    #     glEnd()
    # else:
    #     glBegin(GL_POLYGON)
    #     glColor3f(1, 0.7, 0.4)
    #     glVertex2f(-10, 190)
    #     glVertex2f(10, 190)
    #     glVertex2f(10, 200)
    #     glVertex2f(-10, 200)
    #     glEnd()

    # body
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.3, 1)
    glVertex2f(-40, 160)
    glVertex2f(40, 160)
    glVertex2f(40, 0)
    glVertex2f(-40, 0)
    glEnd()

    # left arm
    glBegin(GL_LINES)
    glColor3f(1, 0.7, 0.4)
    glVertex2f(-40, 140)
    glVertex2f(-70, 10)
    glEnd()

    # right arm
    glBegin(GL_LINES)
    glVertex2f(40, 140)
    glVertex2f(70, 270)
    glEnd()

    # balloons
    drawBalloons(offset)

    glFlush()


def keyboardFunction(key, x, y):
    if(ord(key) == 32):
        offset=0
        while(offset < 500):
            buildScene(offset)
            offset += 0.1

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    buildScene(0)
    glFlush()

def main():
    init()
    glutDisplayFunc(lambda: display())
    glutKeyboardFunc(keyboardFunction)
    glutMainLoop()

if __name__ == '__main__':
    main()