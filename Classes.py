import pygame
import os
import random
import math



class Enemy(pygame.sprite.Sprite):
    # Enemies spawn at start of map and moves towards exit
    def __init__(self,x,y,hp,mapSpec):
        pygame.sprite.Sprite.__init__(self)
        self.hp = hp
        self.pathing = getPath(mapSpec)
        
    
    def update(self):
        #move towards exit