from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 


def midPointCircle(xc, yc, r): 

    glColor3f(255.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    x = r 
    y = 0  

    glVertex2f(x+xc,y+yc)

    if (r > 0) : 
        
        glVertex2f(x+xc,-y+yc)
        glVertex2f(y+xc,x+yc)
        glVertex2f(y+xc,x+yc)
        glVertex2f(-y+xc,x+yc)
 
    P = 1 - r  
  
    while x > y: 
      
        y += 1
 
        if P <= 0:  
            P = P + 2 * y + 1
 
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y): 
            break
 
        glVertex2f(x+xc,y+yc)  
        glVertex2f(-x+xc,y+yc)  
        glVertex2f(x+xc,-y+yc)  
        glVertex2f(-x+xc,-y+yc)  
         

        if x != y: 
            glVertex2f(y+xc,x+yc)  
            glVertex2f(-y+xc,x+yc)  
            glVertex2f(y+xc,-x+yc)  
            glVertex2f(-y+xc,-x+yc) 

    glEnd()
    glFlush()

def nonPolarCircle(xc, yc, radius):

    glColor3f(255.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    x = xc - radius
    t = xc + radius

    glVertex2f(x, yc)
    glVertex2f(t, yc)

    factor = 7500
    increment = 1 / factor
    x += increment

    while x < t:
        offset = math.sqrt(radius * radius - (x - xc) * (x - xc))
        glVertex2f(x, yc + offset)
        glVertex2f(x, yc - offset)
        x += increment

    glEnd()
    glFlush()

def polarCircle(xc, yc, radius):

    glColor3f(255.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    theta = 0
    factor = 500
    increment = 1 / factor
    t = math.pi / 4

    while (theta <= t):

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, -y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(y + xc, x + yc)
        glVertex2f(-y + xc, -x + yc)
        glVertex2f(-y + xc, x + yc)
        glVertex2f(y + xc, -x + yc)
        theta += increment

    glEnd()
    glFlush()



def main():
    print("\nPlot a circle")
    print("1. Using mid-point circle drawing algorithm")
    print("2. Polar generation")
    print("3. Non-Polar Generation\n\n")
    choice = input("Enter Choice : ")

    while True:
        if (int(choice) > 3 or int(choice) < 1):
            print("Invalid choice")
        else:
            break

    x = int(input("\nEnter x coordinate of center : "))
    y = int(input("Enter y coordinate of center : "))
    r = int(input("Enter Radius : "))

    if int(choice) == 1:

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Midpoint Circle Drawing Algorithm")
        glutDisplayFunc(lambda: midPointCircle(x,y,r)) 
        glutIdleFunc(lambda: midPointCircle(x,y,r))
        init()
        glutMainLoop()

    elif int(choice) == 2:

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot Circle using Polar Circle")
        glutDisplayFunc(lambda: polarCircle(x,y,r)) 
        glutIdleFunc(lambda: polarCircle(x,y,r))
        init()
        glutMainLoop()

    
    else:

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Non Polar Circle")
        glutDisplayFunc(lambda: nonPolarCircle(x,y,r)) 
        glutIdleFunc(lambda: nonPolarCircle(x,y,r))
        init()
        glutMainLoop()

if __name__ == '__main__':
    main()
