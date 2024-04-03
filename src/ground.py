import pygame

class Ground(pygame.sprite.Sprite):
  def __init__(self, image_path):
    super().__init__()
    self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))
    self.rect = self.image.get_rect()

  def draw(self, screen, x, y):
    screen.blit(self.image, (x, y))
