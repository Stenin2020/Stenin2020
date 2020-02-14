from graph import *
import math

brushColor("cyan")
rectangle(100,100,500,400)
 

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
    penColor("yellow")
    penSize(11)
    for x in range(101,500):
        y=math.sin(x/10)
        y3=int(y2+5*y)
        point(x,y3)
    
    
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
            circle(x+r*i-r/2*ii,y+r*ii,r)
             
def sun(x,y,r):
    """
    Нарисуем солнце
    x,y,r координаты на небосводе и видимый радиус
    """
    
    penColor("yellow")
    brushColor("yellow")
    circle(x,y,r)

sea(220,300)
sheep(470,240,160)
sheep(300,230,80)
umbrella(200,360,100)
umbrella(300,330,60)
cloud(130,120,10)
cloud(250,140,20)
cloud(150,180,15)
sun(450, 150, 30)




run()
