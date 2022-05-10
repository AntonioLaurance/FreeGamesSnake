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

from turtle import *
from random import choice, randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ["purple", "green", "blue", "pink", "orange"]
color_elegido = choice(colors)

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
        square(body.x, body.y, 9, color_elegido)

    # ¿Qué pasaria si le sumo a la x de la comida 10 pixeles?
    # food.x += 10
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def move_food():
    op = randrange(1, 4)

    if op == 1:
        food.y += 10
    elif op == 2:
        food.y -= 10
    elif op == 3:
        food.x += 10
    elif op == 4:
        food.x -= 10

       
    if food.x >= -200:
        food.x += 20
    elif food.x <= -190:
        food.x -= 20
    elif food.y <= -200:
        food.y += 20
    elif food.y <= 190:
        food.y -= 20

    new_vector = vector(food.x, food.y)

    food.move(new_vector)
    # square(food.x, food.y, 9, 'green')
    update()
    ontimer(move_food, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
# move_food()
done()

