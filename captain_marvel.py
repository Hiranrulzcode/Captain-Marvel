import pygame
import time
from pygame.locals import *

pygame.init()
WIDTH=1500
HEIGHT=1500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
object_x=0
object_y=0
keys=[False,False,False,False]
captain_marvel=pygame.image.load("Pro Python Game Development 2/captain_marvel/captain_marvel.png")
bg=pygame.image.load("Pro Python Game Development 2/captain_marvel/avengers_tower.webp")


run=True
while run:
    screen.blit(bg,(0,0))
    screen.blit(captain_marvel,(object_x,object_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:

            if event.key==K_UP:
                keys[0]=True
        
            elif event.key==K_LEFT:
                keys[1]=True

            elif event.key==K_DOWN:
                keys[2]=True
        
            elif event.key==K_RIGHT:
                keys[3]=True
            
        if event.type==pygame.KEYUP:

            if event.key==K_UP:
                keys[0]=False
        
            elif event.key==K_LEFT:
                keys[1]=False

            elif event.key==K_DOWN:
                keys[2]=False
        
            elif event.key==K_RIGHT:
                keys[3]=False
    
    if keys[0]:
        object_y=object_y-8
    
    if keys[1]:
        object_x=object_x-8
    
    if keys[2]:
        object_y=object_y+8
    
    if keys[3]:
        object_x=object_x+8
            
