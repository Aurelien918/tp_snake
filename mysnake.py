from random import randint
import pygame as pg


def draw_board():
    pg.init()
    screen=pg.display.set_mode((600,600))
    while True:
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
        pg.display.update()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
            elif event.type==pg.KEYDOWN and event.key==pg.K_q :
                pg.quit()


draw_board()
draw_snake(snake)

#IL y a 15*15=225 rectangles blancs dessinés par image


