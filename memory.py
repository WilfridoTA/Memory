"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
"""se agregan caracteres especiales para las tiles"""
symbols=['!', '>>', '<<', '>', '<', '¬', '°', '|', ';', ',', ':', '.', '-', '^', ']', '}', '[', '{', '~', '*', '+', '¡', '¿', '?', '=', ')', '(', '/', '&', '%', '$', '#']
tiles = symbols * 2
"""Agregación del contador de taps"""
state = {'mark': None, 'taps': 0}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    """Incrementa contador de taps"""
    state['taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()

    """Mostrar taps"""
    up()
    goto(-180, 200)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 16, 'normal'))

    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
	
	#Se centran los numeros que se muestran al voltear los cuadrados
        goto(x + 10, y + 5)
	
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    #Revisar si todos los cuadrados han sido volteados
    if all(not h for h in hide):
    	goto(0, 0)
    	color('white')
	#Al estar todos volteados se muestra el texto GANASTE en el centro de la pantalla
    	write("GANASTE!", align="center", font=('Arial', 50, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(600, 600, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
