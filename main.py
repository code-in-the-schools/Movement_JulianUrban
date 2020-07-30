import pygame
import os

img_path = os.path.join('player.png')

class Character(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    Character.image = pygame.image.load('player.png')
    self.image = Character.image
    self.image = pygame.transform.scale(self.image,(100,100))
    self.height = 100
    self.width = 100

    self.x = 50
    self.y = 50
    self.hitbox = (self.x, self.y, 55, 55)

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def movement(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] and self.y < 500 - self.height - 1:
      self.y += 1
    if key[pygame.K_UP] and self.y > 1:
      self.y -= 1
    if key[pygame.K_LEFT] and self.x > 1:
      self.x -= 1
    if key[pygame.K_RIGHT] and self.x < self.width - 1 - 55:
      self.x += 1



pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((int(screen_width),int(screen_height)))

pikachu = Character()
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  screen.fill((255, 255, 255))
  pikachu.movement()
  pikachu.draw(screen)
  pygame.display.update()
  clock.tick(60)
