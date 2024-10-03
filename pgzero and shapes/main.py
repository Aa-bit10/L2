import pgzrun 
from random import randint 

WIDTH = 300
HEIGHT = 300
TITLE = "aaron"

def draw():
    r = 255
    g = 0 
    b = randint(120,255)
    width = WIDTH
    height = HEIGHT - 200


    screen.fill("purple")
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 150,150
        screen.draw.rect(rect,(r,g,b))
        g += 10
        r -= 10
        width -= 10
        height += 10
    
def update():
    pass

pgzrun.go()

