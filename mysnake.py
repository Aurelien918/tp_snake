from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

while True:
    clock.tick(1)

    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
        elif event.type==pg.KEYDOWN and event.key==pg.K_q :
            pg.quit()
    

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()

    #On ne pouvait pas fermer la fenetre avec la croix car la boucle était infinie et il n'y avait pas de condition pour finir la boucle