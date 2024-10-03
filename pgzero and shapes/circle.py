import pgzrun 
from random import randint 

WIDTH = 300
HEIGHT = 300
TITLE = "circle"
def draw():
    r = 255
    g = 0 
    b = randint(120,255)

    screen.fill("purple")       
    screen.draw.circle((150,150),50,(r,g,b))
    
       
    
def update():
    pass
pgzrun.go()