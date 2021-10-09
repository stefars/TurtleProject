from turtle import *
screen=getscreen()
screen.setup(800,800)
speed(0)
sqr_len=40
health_x = 170

def Lyla():
    up()
    goto(30,0)
    down()
    for i in range(5):
        dot(120,"#e35d6a")
        up()
        left(70)
        forward(100)
        down()

    up()
    goto(0,0)
    down()
    dot(130,"#ffbdbd")


    up()
    goto(20,5)
    down()
    dot(20,"white")
    up()
    goto(20,5)
    down()
    dot(8)



    up()
    goto(22,5)
    down()
    dot(20,"white")
    up()
    goto(22,5)
    down()
    dot(8)

    up()
    goto(-70,50)
    down()

    pencolor("#d9534f")
    pensize(3)
    fillcolor("#ff6f69")
    begin_fill()
    circle(110,25)
    right(110)
    circle(-25,170)
    end_fill()
    hideturtle()
    done()

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

def game_over():
    screen.bgpic("game_over.png")
    exit()

def you_won():
    screen.bgpic("you_won.png")
    exit()

from turtle import *

screen = Screen()
screen.bgcolor("#fffc86")
screen.bgpic("background.png")

def clear():
    screen.delay(2000)
    screen.bgpic("background.png")
    undo()
    screen.bgpic("background2.png")

def story():
    penup()
    setpos(-370, -330)
    pendown()
    write ('There was once a flower named Lyla who was\nvery popular among the garden’s residents \nlike Larry the Snail or Sony the Garden Gnome.', font=("Helvetica", 20, 'normal'))
    clear()
    write('During the day, she’s very happy and cheerful,\n feeding off sunlight and social interactions with her peers.', font=("Helvetica", 20, "normal"))

hideturtle()
speed(0)


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

    #prep for health
    penup()
    pen(pencolor="#C0FF00",fillcolor="#C0FF00",pensize = 2)

    #Draw Health stat
    sqr_len=40
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
    
Stats_Draw()
Lyla()
story()
mainloop()