import pygame as p, random

class Asteroid(p.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = p.image.load('Zoom.jpeg')
    self.image = p.transform.smoothscale(self.image, (50,100))
    self.rect = self.image.get_rect()
    self.rect.center = (random.randint(0, 800), random.randint(0, 600))
    self.speed = p.math.Vector2(0,3)
    self.speed.rotate_ip(random.randint(0, 360))

  def update(self):
    self.rect.move_ip(self.speed)
    self.image
    self.screen_info = p.display.Info()
    self.rect.move_ip(self.speed)

    if  self.rect.bottom > 800:
      self.speed[1] *= -1
      self.image = p.transform.flip(self.image, False, True)
      self.rect.move_ip(0, self.speed[1])

    elif  self.rect.top < 0:
      self.speed[1] *= -1
      self.image = p.transform.flip(self.image, False, True)
      self.rect.move_ip(0, self.speed[1])

    if  self.rect.right > 900:
      self.speed[0] *= -1
      self.image = p.transform.flip(self.image, True, False)
      self.rect.move_ip(self.speed[0], 0)

    if  self.rect.left < 0:
      self.speed[0] *= -1
      self.image = p.transform.flip(self.image, True, False)
      self.rect.move_ip(self.speed[0], 0)

