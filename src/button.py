import pygame
from settings import SCREEN_WIDTH

class Button():
  def __init__(self, image_path):
    self.image = pygame.transform.scale(pygame.image.load(image_path), (30, 30))
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH // 2
    self.rect.y = 200

  def draw(self, screen, game_over):
    if game_over:
      screen.blit(self.image, self.rect)
