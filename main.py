import pygame
from Ship import *
from Asteroid import *
from pygame import mixer 


pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)


mixer.init() 
mixer.music.load("song.mp3") 
mixer.music.set_volume(0.7)  
mixer.music.play() 


NumLevels = 4
Level = 1
AsteroidCount = 2
Player = Ship((20, 300))
Asteroids = pygame.sprite.Group()

def init():
  Player.reset((20, 300))
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid())


def main():
  init()
  while Level <= NumLevels:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          Player.speed[0] = 40
        if event.key == pygame.K_LEFT:
          Player.speed[0] = -40
          Player.left()
        if event.key == pygame.K_UP:
          Player.speed[1] = -40    
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 40  
        if event.key == pygame.K_r:
          Player.speed[0] = 0
          Player.speed[1] = 0
          Player.center = (20, 300)
      if event.type == pygame.KEYUP:
        Player.speed[0] = 0
        if event.key == pygame.K_LEFT:
          Player.speed[0] = 0
        if event.key == pygame.K_UP:
          Player.speed[1] = 0    
        if event.key == pygame.K_DOWN:
          Player.speed[1] = 0  
    Player.update()
    Asteroids.update()
    screen.fill(color)
    screen.blit(Player.image, Player.rect)
    Asteroids.draw(screen)
    pygame.display.flip()

if __name__ == '__main__':  
  main()