from random import randint
import pygame as pg

def draw_snake(snake):
    for a in snake:
        x,y=a[0]*20,a[1]*20
        width, height = 20, 20
        color = (255, 0, 0)
        rect = pg.Rect(x, y, width, height)
        pg.draw.rect(screen, color, rect)
    
    

snake = [
   (10, 15),
   (11, 15),
   (12, 15),
]


def draw_board():
    screen.fill((0,0,0))
    for ligne in range(32):
        for colonne in range(32):
            if (ligne + colonne) % 2 == 0:
                couleur = (255,255,255)
            else:
                couleur = (0,0,0)
            x = colonne * 20
            y = ligne * 20
            pg.draw.rect(screen, couleur, (x, y, 20, 20))
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
        elif event.type==pg.KEYDOWN and event.key==pg.K_q :
            pg.quit()
direction=(1,0)

def move_snake(snake, direction):
    snake.pop(0)
    snake.append((snake[-1][0]+direction[0],snake[-1][1]+direction[1]))
    return snake

assert move_snake([(10, 15), (11, 15), (12, 15)], (1, 0)) == [(11, 15), (12, 15), (13, 15)]
assert move_snake([(10, 15), (11, 15), (12, 15)], (0, -1)) == [(11, 15), (12, 15), (12, 14)]



pg.init()
screen=pg.display.set_mode((600,600))
clock=pg.time.Clock()
while True:
    clock.tick(2)
    draw_board()
    draw_snake(snake)
    move_snake(snake,direction)
    pg.display.update()

#Quand le serpent atteint le bord de la fenêtre il continue à avancer jusqu'à disparaître
    








