#Python 3.7 works

import pygame
import os
import sys
import random
from Classes import *


windowWidth = 600
windowHeight = 800
window = pygame.display.set_mode((windowWidth,windowHeight))
clock = pygame.time.Clock()
gameSpeed = 30

def towDef():
    