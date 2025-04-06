import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 500
TITLE = "TREASURE"

soldier=Actor("soldier")
soldier.pos=randint(50,750),randint(50,450)
crate=Actor("crate")
crate.pos=randint(50,750),randint(50,450)
score=0

def draw():
    screen.blit("1.jpg",(0,0))
    soldier.draw()
    crate.draw()

def update():
    global score
    if keyboard.left: 
        if soldier.x>0:
            soldier.x-=10
    elif keyboard.right:
        soldier.x+=10
    elif keyboard.up:
        soldier.y-=10
    elif keyboard.down:
        soldier.y+=10
    if soldier.colliderect(crate):
        soldier.pos=randint(50,750),randint(50,450)    
        crate.pos=randint(50,750),randint(50,450)
        score+=1

pgzrun.go()
