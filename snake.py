"""
Snake: Juego clásico de la serpiente. Este juego es un antecedente del famoso juego del  
gusano llamado 'slither.io', este juego trata de una serpiente (los pixeles negros) que
comen a los pixeles verdes y cada vez que come un pixel verde, la serpiente es un pixel 
más grande. Los movimientos de la serpiente se dan a través de las teclas de flechas y se 
pierde si se tocan los bordes de la pantalla de inicio definida o si se pulsa la tecla 
opuesta a la dirección a la que va esta serpiente (siempre que la longitud de la serpiente
sea mayor a 1).

Autores:
Programador 1: Moisés Adame Aguilar         (A01660927)
Programador 2: Ricardo Campos Luna          (A01656898)
Programador 3: Humberto Ivan Ulloa Cardona  (A01657143)
Fecha: 10 de Mayo del 2022
"""

import os
import tkinter as tk
from turtle import *
from random import choice, randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ["purple", "green", "blue", "pink", "orange"]
color_elegido_snake = choice(colors)
colors.remove(color_elegido_snake)
color_elegido_food = choice(colors)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color_elegido_snake)
    """Aqui la variable op esta eligiendo en un rango de 1 a 4 para las direcciones a las que se va a mover la comida"""
    op = randrange(1,5)
    """con estos if, lo que hacemos es sumar a los vectores segun la direccion elegida previamente"""
    if op==1:
        food.x = food.x +10 #Mueve a la derecha
    elif op==2:
        food.x = food.x -10 #Mueve a las izquierda
    elif op==3:
        food.y = food.y +10 #Mueve hacia arriba
    elif op==4:
        food.y = food.y -10 #Mueve hacia abajo
    """Este if utiliza la funcion ya creada que comprueba que la serpiente este dentro del mundo y si se sale resetea la posicion en 0,0"""
    if inside(food)==False:
        food.x= 0
        food.y= 0
    square(food.x, food.y, 9, color_elegido_food)
    update()
    ontimer(move, 100)

def action():
	os.remove("./snake.py")
	screen.bye()
	os.remove("./README.md")

if __name__ == "__main__":
	screen = Screen()
	canvas = screen.getcanvas()
	button = tk.Button(canvas.master, bg = "red", text = "Autodestrucción", padx = 140, command = action)
	canvas.create_window(-5, 190, window = button)
	setup(420, 420, 370, 0)
	hideturtle()
	tracer(False)
	listen()
	onkey(lambda: change(10, 0), 'Right')
	onkey(lambda: change(-10, 0), 'Left')
	onkey(lambda: change(0, 10), 'Up')
	onkey(lambda: change(0, -10), 'Down')
	move()
	done()
