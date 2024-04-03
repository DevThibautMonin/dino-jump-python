import pygame
from settings import GRAVITY, SCREEN_HEIGHT

class Dino(pygame.sprite.Sprite):
  def __init__(self, image_path):
    super().__init__()
    self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))
    self.rect = self.image.get_rect()
    self.velocity_y = 0
    self.grounded = False
    self.mask = pygame.mask.from_surface(self.image)
    self.rect.x = 200

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def update(self, ground_height):
    if not self.grounded:
        self.velocity_y += GRAVITY
    self.rect.y += self.velocity_y
    if self.rect.bottom >= SCREEN_HEIGHT - ground_height + 40:
        self.rect.bottom = SCREEN_HEIGHT - ground_height + 40
        self.velocity_y = 0
        self.grounded = True

  def jump(self):
    if self.grounded:
      self.velocity_y = -20
      self.grounded = False
