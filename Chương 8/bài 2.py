print('Sinh viên: Lê Quang Trung')
print('Mã số SV: 235752021610012')

import turtle
import random

window = turtle.Screen()
window.bgcolor("pink")  

star = turtle.Turtle()
star.pensize(3)
star.speed(10)  

colors = ["red", "yellow", "green", "blue", "purple", "orange", "cyan", "pink"]

def draw_star(t, size):
    for i in range(20):
        t.fillcolor(random.choice(colors))  
        t.begin_fill()  
        t.forward(size)
        t.right(144)  
        t.end_fill()  


star.penup()  
star.goto(-50, 0)  
star.pendown()  

draw_star(star, 150)

turtle.done()
