from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-250.0,250.0,-250.0,250.0)

def draw_triangle(a,b,c,m):
    v0=[]
    v1=[]
    v2=[]

    if(m>0):
        v0.append((a[0]+b[0])/2)
        v0.append((a[1]+b[1])/2)
        
        v1.append((a[0]+c[0])/2)
        v1.append((a[1]+c[1])/2)

        v2.append((b[0]+c[0])/2)
        v2.append((b[1]+c[1])/2)

        draw_triangle(a, v0, v1, m-1)
        draw_triangle(b, v2, v0, m-1)
        draw_triangle(c, v1, v2, m-1)

    else:
        glBegin(GL_TRIANGLES)
        glVertex2fv(a);
        glVertex2fv(b);
        glVertex2fv(c);
        glEnd()
        glFlush()

def initiate_drawing(side):
    coord = []
    height = math.sqrt(3) * side / 2

    coord.append([-side, 0])
    coord.append([+side, 0])
    coord.append([0, height])

    iterations = int(math.log2(height))
    draw_triangle(coord[0], coord[1], coord[2], iterations);

def display(side):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    initiate_drawing(side)
    glFlush()

def main():
    print()
    side = int(input("Enter side length of equilateral triangle : "))
    print()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Sierpenski Triangle")
    init()
    glutDisplayFunc(lambda: display(side))
    glutMainLoop()

if __name__ == '__main__':
    main()
