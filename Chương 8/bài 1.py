print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

import turtle
import random


window = turtle.Screen()
window.bgcolor("black")  

painter = turtle.Turtle()
painter.pensize(3)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "white"]

def drawsq(t, s):
    for _ in range(4):
        t.forward(s)
        t.left(90)

for i in range(1, 180):
    painter.pencolor(random.choice(colors))  
    painter.fillcolor(random.choice(colors)) 
    
    painter.begin_fill()
    drawsq(painter, 200)
    painter.end_fill()
    
    painter.left(18)

turtle.done()
