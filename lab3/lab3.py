from graph import *
from math import *

brushColor("cyan")
rectangle(100,100,500,400)
 
windowSize(1000,600)

def sea(y1,y2):
    """
    нарисуем море
    y1 -горизонт
    y2 -урез воды
    """

    brushColor("cyan")
    rectangle(100,100,500,400)
    brushColor("blue")
    rectangle(100,y1,500,400)
    brushColor("yellow")
    rectangle(100,y2,500,400)

def sheep(x,y,l):
    """
    Нарисуем корабль
    x,y,l координаты носа и длина корабля
    """
    A=(x,y)
    B=(int(x-l),y)
    D=(int(x-0.9*l),int(y+0.1*l))
    C=(int(x-0.3*l),int(y+0.1*l))
    E=(int(x-0.6*l),y)
    F=(int(x-0.6*l),int(y-0.5*l))
    N=(int(x-0.5*l),int(y-0.25*l))
    M=(int(x-0.3*l),int(y-0.25*l))
    penColor("brown")
    brushColor("brown")
    polygon([A,B,D,C,A])
    penColor("black")
    penSize(5)
    line(E[0],E[1],F[0],F[1])
    penColor("green")
    brushColor("green")
    polygon([E,N,F,M,E])
    penColor("black")
    penSize(2)
    brushColor(250,250,250)
    circle(x-0.25*l,y+0.05*l,4)
    

def umbrella(x,y,h):
    """
    Нарисуем зонтик
    x,y,h координаты основания и высота
    """
    penColor("black")
    penSize(1)
    brushColor("red")
    A=y-h
    B=y-int(0.8*h)
    C=y
    D=int(0.1*h)
    polygon([(x-h//2,B),(x,A),(x+h//2,B),(x-h//2,B)])
    for i in range(1,10):
        line (x,A,x-h//2+D*i,B)
    penColor("brown")
    penSize(7)
    line (x,y,x,B)
          
def cloud(x,y,r):
    """
    нарисуем облако
    x,y,r координаты и радиус левого клубочка
    """
    
    penColor("black")
    penSize(1)
    brushColor(250,250,250)
    for ii in range (2):
        for i in range(3+ii):
            circle(x+10*i-5*ii,y+10*ii,r)
             
def sun(x,y,r):
    """
    Нарисуем солнце
    x,y,r координаты на небосводе и видимый радиус
    """
    
    penColor("yellow")
    brushColor("yellow")
    circle(x,y,r)

sea(220,300)
sheep(440,240,160)
umbrella(200,360,100)
cloud(150,150,10)
sun(450, 150, 30)




run()
