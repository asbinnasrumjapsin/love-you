from re import X 
from tkinter import Y
from tkinter.ttk import Style
import turtle
from turtle import *

l = Screen()
l.bgcolor("black")

t = turtle.Turtle()
t.pencolor("white")

def curve():
  for i in range(200):
    t.rt(1)
    t.fd(1)

def love():
  t.fillcolor("red")
  t.begin_fill()
  t.lt(140)
  t.fd(113)
  curve()
  t.lt(120)
  curve()
  t.fd(112)
  t.end_fill()

love()
t.ht()

def write(pesan,pos):
  X, Y = pos
  t.penup()
  t.goto(X,Y)
  t.color("white")
  Style=("arial", 18, "bold")
  t.write(pesan, font=Style)

write("I",(-68,95))
write("L",(-55,95))
write("O",(-42,95))
write("V",(-25,95))
write("E",(-10,95))
write("Y",(10,95))
write("O",(26,95))
write("U",(45,95))

l.mainloop()
