import turtle
import random

print("Sinh vien : Lê Quang Trung")
print("Ma so SV: 235752021610012")

colors = ["red", "green", "blue", "yellow", "purple", "cyan", "orange", "pink", "violet", "indigo"]

window = turtle.Screen()
window.bgcolor("black")  

painter = turtle.Turtle()
painter.pensize(3)  
painter.speed(10)  
def draw_circle(radius):
    color = random.choice(colors)  
    painter.pencolor(color)  
    painter.fillcolor(color) 
    painter.begin_fill()  
    painter.circle(radius)  
    painter.end_fill()  

for i in range(18):  
    draw_circle(100 + i * 10)  
    painter.right(20)  

turtle.done()
