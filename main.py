import pygame, sys
from pygame.locals import *
pygame.init()#initates pygame
WINDOW_SIZE = (400,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)#initate the WINDOW_SIZE
running = True
while running:
  for event in pygame.event.get():#getting all the keyboard inputs from user
    if event.type == QUIT:#if one of those inputs is the user pressing the quit button
      pygame.quit()#it will terminate ptgame
      sys.exit()