from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 


def nonPolarEllipse(xc, yc, xr, yr):

    glColor3f(255.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    x = xc-xr
    t = xc+xr
    glVertex2f(x, yc)
    glVertex2f(t, yc)

    factor = 500
    increment = 1 / factor
    x += increment

    while x < t:
        offset = yr * math.sqrt(1 - (((x-xc)/xr) * ((x-xc)/xr)))
        glVertex2f(x, yc + offset)
        glVertex2f(x, yc - offset)
        x += increment

    glEnd()
    glFlush()

def polarEllipse(xc, yc, xr, yr):

    glColor3f(255.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    theta = 0
    factor = 500
    increment = 1 / factor
    t = math.pi / 2

    while (theta <= t):

        x = xr * math.cos(theta)
        y = yr * math.sin(theta)
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, -y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        theta += increment

    glEnd()
    glFlush()



def main():
    print("\nPlot an ellipse")
    print("1. Polar Generation Algorithm")
    print("2. Non-Polar Generation Algorithm")
    choice = input("Enter Choice : ")

    while True:
        
        if (int(choice) > 2 or int(choice) < 1):
            print("Invalid choice")
            choice = input("Enter Choice : ")
        else:
            break

    x = int(input("\nEnter x coordinate of center : "))
    y = int(input("Enter y coordinate of center : "))
    xr = int(input("Enter x-radius : "))
    yr = int(input("Enter y-radius : "))

    if int(choice) == 1:

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Polar Ellipse")
        glutDisplayFunc(lambda: polarEllipse(x,y,xr,yr)) 
        init()
        glutMainLoop()
    
    else:

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Non Polar Ellipse")
        glutDisplayFunc(lambda: nonPolarEllipse(x,y,xr,yr))
        init()
        glutMainLoop()

if __name__ == '__main__':
    main()
