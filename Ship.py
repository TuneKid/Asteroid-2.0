import pygame

class Ship(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load('Godspeed.jpg')
    self.image = pygame.transform.smoothscale(self.image, (100,150))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,0)

  def update(self):
    self.rect.move_ip(self.speed)
  def left(self):
    self.turn = pygame.transform.rotate(self.image, 180)

    def reset(self, pos):
      self.rect.center = pos
