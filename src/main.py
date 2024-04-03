import pygame
import dino
import ground
import cactus
import button
import os
import random
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, GRAVITY

pygame.init()

dirname = os.path.dirname(__file__)
ground_path = os.path.join(dirname, "../assets/ground.png")
dino_path = os.path.join(dirname, "../assets/dino.png")
cactus_path = os.path.join(dirname, "../assets/cactus.png")
restart_path = os.path.join(dirname, "../assets/restart.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Jump")
run = True
score = 0
font_size = 60
font = pygame.font.SysFont("Bauhaus 93", font_size)
text_color = (0, 0, 0)
pass_cactus = False
game_over = False

ground = ground.Ground(ground_path)
dino = dino.Dino(dino_path)
cactus_group = pygame.sprite.Group()
restart_button = button.Button(restart_path)

last_cactus = pygame.time.get_ticks() - random.randint(1500, 5000)

def draw_text(text, font, text_color, x, y):
  img = font.render(text, True, text_color)
  screen.blit(img, (x, y))

def reset_game():
  cactus_group.empty()
  score = 0
  return score

while run:
  screen.fill("white")
  clock.tick(FPS)

  time_now = pygame.time.get_ticks()
  if time_now - last_cactus > random.randint(1000, 5000):
    last_cactus = time_now
    new_cactus = cactus.Cactus(cactus_path, ground.image.get_height())
    new_cactus.rect.x = SCREEN_WIDTH
    cactus_group.add(new_cactus)

  for i in range(SCREEN_WIDTH // ground.image.get_width() + 1):
    ground.draw(screen, i * ground.image.get_width(), SCREEN_HEIGHT - ground.image.get_height())
    
  for cact in cactus_group:
    if cact.rect.right < dino.rect.left and not cact.passed:
      score += 1
      cact.passed = True

  draw_text(str(score), font, text_color, int(SCREEN_WIDTH / 2), 20)

  if not game_over:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      dino.jump()

  if pygame.sprite.spritecollide(dino, cactus_group, False, pygame.sprite.collide_mask):
    game_over = True

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN and game_over:
        mouse_pos = event.pos
        if restart_button.rect.collidepoint(mouse_pos):
            score = reset_game()
            game_over = False

  dino.update(ground.image.get_height())
  dino.draw(screen)

  if not game_over:
    cactus_group.update()
  cactus_group.draw(screen)

  restart_button.draw(screen, game_over)

  pygame.display.update()
