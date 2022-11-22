import pygame as p
BLACK=[0,0,0]
WHITE=[255,255,255]
RED=[255,0,0]
GREEN=[0,255,0]
GRAY=[120,120,120]
p.init()
screen=p.display.set_mode((300,300))
p.display.set_caption('NGC Research Checker')
p.draw.rect(screen,GRAY,(6,10,88,100))
p.draw.rect(screen,GREEN,(106,10,88,100))
p.draw.rect(screen,RED,(206,10,88,100))
p.display.update()
while True:
    print("egg")
