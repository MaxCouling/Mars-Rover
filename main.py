import pygame, sys, random
from pygame.locals import *
pygame.init()#initates pygame
WINDOW_SIZE = (600,400)
clock = pygame.time.Clock()#imports the time
screen = pygame.display.set_mode(WINDOW_SIZE,0,32)#initate the WINDOW_SIZE

asteroids = []

class Asteroid:
  def __init__(self, pos_x, pos_y):
    self.pos = [pos_x, pos_y]
  def update(num):
    for i in range(num):
      asteroid_location = Asteroid(random.randint(0,568), random.randint(400,4000))
      asteroids.append(asteroid_location)




#loading images and setting display
pygame.display.set_caption("Mars Rover")
player_image = pygame.image.load("player.png")
icon = pygame.image.load("logo.png")
asteroid_image = pygame.image.load("asteroid.png")
pygame.display.set_icon(icon)


#variables
moving_right = False
moving_left = False
moving_down = False
moving_up = False
running = True
player_location = [50,50]#sets starting

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())#playerhitbox

test_rect = pygame.Rect(100,100,100,50)#testing retangle hitbox

Asteroid.update(15)

#moving around minigame
while running:
  pygame.display.update()
  screen.fill((146,244,255))
  screen.blit(player_image,player_location)#player location


  player_rect.x = player_location[0]
  player_rect.y = player_location[1]

  if player_rect.colliderect(test_rect):
    pygame.draw.rect(screen, (255,0,0), test_rect)
  else:
    pygame.draw.rect(screen, (0,0,0), test_rect)


  for asteroid_location in asteroids:
    screen.blit(asteroid_image, asteroid_location.pos)#astriod location
    asteroid_location.pos[1] -= 6



  if moving_right:
    player_location[0] += 4
  if moving_left:
    player_location[0] -= 4
  if moving_down:
    player_location[1] += 4
  if moving_up:
    player_location[1] -= 4
  
  for event in pygame.event.get():#getting all the keyboard inputs from user
    if event.type == QUIT:#if one of those inputs is the user pressing the quit button
      print("Exited")#prints ecited into the console
      pygame.quit()#it will terminate ptgame
      sys.exit()
    if event.type == KEYDOWN:#movemtnt code
      if event.key == K_RIGHT:
        moving_right = True
      if event.key == K_LEFT:
        moving_left = True
      if event.key == K_DOWN:
        moving_down = True
      if event.key == K_UP:
        moving_up = True
    if event.type == KEYUP:
      if event.key == K_RIGHT:
        moving_right = False
      if event.key == K_LEFT:
        moving_left = False
      if event.key == K_DOWN:
        moving_down = False
      if event.key == K_UP:
        moving_up = False
  
  
  if player_location[0] <= 0:#boundries in the game
    player_location[0] = 0
  elif player_location[0] >= 568:
    player_location[0] = 568
  
  
  clock.tick(60)#making the game run at 60fps by limiting the amount of.0