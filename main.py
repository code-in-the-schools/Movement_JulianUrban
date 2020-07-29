import pygame
import os

img_path = os.path.join('player.png')

class Character(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    Character.image = pygame.image.load('player.png')
    self.image = Character.image
    #self.image = pygame.transform.scale(self.image(50,50))

    self.x = 50
    self.y = 50
    self.hitbox = (self.x, self.y, 55, 55)

    self.movex = 0
    self.movey = 0

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
  
  #adding pixels to sprite position
  def control(self, x, y): 
    self.movex += x
    self.movey += y

  #for updating sprite position on keypress
  def update(self):
    self.rect.x = self.rect.x + self.movex
    self.rect.y = self.rect.y + self.movey



pygame.init()
screen_width = 600
screen_height = 600
steps = 10
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
  pikachu.draw(screen)
  pygame.display.update()
  clock.tick(60)

  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
      print("Left")
      pikachu.control(-steps,0)
    if event.key = pygame.K_RIGHT:
      print("Right")
      pikachu.control(steps,0)
