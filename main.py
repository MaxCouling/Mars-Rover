import pygame, sys, random
import time
from pygame.locals import *
pygame.init()#initates pygame
clock = pygame.time.Clock()#imports the time
screen = pygame.display.set_mode((600,400))#initate the WINDOW_SIZE

asteroids = []#THIS WILL HOLD ALL THE OBJECTS

class Asteroid:
  def __init__(self, pos_x, pos_y):#THE TWO THINGYS INSIDE THE OBJCET
    self.pos = [pos_x, pos_y]
  def update(num):
    for i in range(num):
      asteroid_location = Asteroid(random.randint(0,568), random.randint(400,4000))#change this
      asteroids.append(asteroid_location)

class Player:
  def __init__(self,pos_x,pos_y):
    self.immune = False
    self.moving_right = False
    self.moving_left = False
    self.moving_down = False
    self.moving_up = False

    self.pos= [pos_x,pos_y]
  def update(self):

 
    for event in pygame.event.get():#getting all the keyboard inputs from user
      if event.type == QUIT:#if one of those inputs is the user pressing the quit button
        print("Exited")#prints ecited into the console
        pygame.quit()#it will terminate ptgame
        sys.exit()
        
      if event.type == KEYDOWN:#movemtnt code
        if event.key == K_RIGHT:
          self.moving_right = True
        if event.key == K_LEFT:
          self.moving_left = True
        if event.key == K_DOWN:
          self.moving_down = True
        if event.key == K_UP:
          self.moving_up = True

      if event.type == KEYUP:
        if event.key == K_RIGHT:
          self.moving_right = False
        if event.key == K_LEFT:
          self.moving_left = False
        if event.key == K_DOWN:
          self.moving_down = False
        if event.key == K_UP:
          self.moving_up = False

      if self.moving_right:
        self.player_location.pos[0] += 4
      if self.moving_left:
        self.player_location.pos[0] -= 4
      if self.moving_down:
        self.player_location.pos[1] += 4
      if self.moving_up:
        self.player_location.pos[1] -= 4


  


#loading images and setting display
black = (0,0,0)#tuple
pygame.display.set_caption("Mars Rover")
player_image = pygame.image.load("player.png")
icon = pygame.image.load("logo.png")
asteroid_image = pygame.image.load("asteroid.png")
pygame.display.set_icon(icon)



#variables
running = True 
damage = 0
num_of_asteroids = 15
player_location = [50,50]#sets starting
Asteroid.update(num_of_asteroids)
player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())#playerhitbox
myFont = pygame.font.SysFont("Times New Roman", 18)

p = Player(50,50)

#moving around minigame
while running:
  pygame.display.update()
  screen.fill((146,244,255))
  p.update()
  screen.blit(player_image,player_location)#player location


  player_rect.x = player_location[0]#updates the playerlocaiton hitbox to follow the player image
  player_rect.y = player_location[1]

  damage_display = myFont.render(str(damage), 1, black)
  screen.blit(damage_display, (520, 30))

  
    
    


  for asteroid_location in asteroids:
    asteroid_rect = pygame.Rect(asteroid_location.pos[0], asteroid_location.pos[1], asteroid_image.get_width(), asteroid_image.get_height())
    screen.blit(asteroid_image, asteroid_location.pos)#astriod location
    asteroid_location.pos[1] -= 6#IMPORTANT!!!!!!!! HOW TO GET THE X AND Y VARIABLES FROM OBJECT TYPE BEAT
    asteroid_rect.x = asteroid_location.pos[0]
    asteroid_rect.y = asteroid_location.pos[1]
    if player_rect.colliderect(asteroid_rect):
      damage += 1

    
    


  


  
  
  
  
  
  if player_location[0] <= 0:#boundries in the game for x axis
    player_location[0] = 0
  elif player_location[0] >= 568:
    player_location[0] = 568
  
  
  clock.tick(60)#making the game run at 60fps by limiting the amount of.0