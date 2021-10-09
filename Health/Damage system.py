from turtle import *

screen = Screen()

screen.setup(800,800,startx=0,starty=0)

hideturtle()
speed(0)
sqr_len=40
health_x = 170

#Draws Stats

def Stats_Draw():
    #Prep for box
    pen(pencolor="black", fillcolor="black", pensize=3)
    penup()
    setpos(165,350)
    pendown()
    begin_fill()
    x=220
    y=85

    #Draw box for stats
    for i in range (0,2):
        forward(x)
        left(90)
        forward(y)
        left(90)
    end_fill()

    #Prep for health
    penup()
    pen(pencolor="#C0FF00",fillcolor="#C0FF00",pensize = 2)

    #Draw Health stat
    
    setpos(170,355)
    for i in range (0,5):
        begin_fill()
        for j in range(0,2):
            forward(sqr_len)
            left(90)
            forward(sqr_len)
            left(90)
        end_fill()
        forward(sqr_len+3)
    penup()

#Drains health

def Drain_Health():
    penup()
    pen(pencolor="black", fillcolor="black",pensize=2, speed=0)
    setpos(health_x,355)
    pendown()
    begin_fill()
    for i in range(0,2):
        forward(sqr_len)
        left(90)
        forward(sqr_len)
        left(90)
    end_fill()



Stats_Draw()


raspuns = 2

#Answer comparasion and health drainage if wrong
v= input()
if raspuns != v:
    Drain_Health()
    health_x +=sqr_len+3
    if health_x == 385:
        circle()
       
     



     

done()






