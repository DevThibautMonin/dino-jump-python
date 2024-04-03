import pygame
from settings import SCREEN_HEIGHT

class Cactus(pygame.sprite.Sprite):
  def __init__(self, image_path, ground_height):
    super().__init__()
    self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))
    self.rect = self.image.get_rect()
    self.rect.bottom = SCREEN_HEIGHT - ground_height + 40
    self.mask = pygame.mask.from_surface(self.image)
    self.passed = False

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def update(self):
     self.rect.x -= 8
