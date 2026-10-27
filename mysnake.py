from random import randint
import pygame as pg

def draw_board():
    pg.init()
    screen=pg.display.set_mode((600,600))
    while True:
        screen.fill((0,0,0))
        for i in range(0,15):
            for j in range(0,15):
                x, y= 40*i, 40*j
                width, height = 20, 20
                color = (255, 255, 255)
                rect = pg.Rect(x, y, width, height)
                pg.draw.rect(screen, color, rect)
        pg.display.update()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
            elif event.type==pg.KEYDOWN and event.key==pg.K_q :
                pg.quit()

draw_board()
#IL y a 15*15=225 rectangles blancs dessinés par