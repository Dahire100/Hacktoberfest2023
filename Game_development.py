import pygame
import random

pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game
pygame.display.set_caption("My Game")

# Create a player object
class Player(pygame.sprite.Sprite):
  def _init_(self):
    super(Player, self)._init_()
    self.image = pygame.image.load("player.png")
    self.rect = self.image.get_rect()
    self.rect.center = (screen_width / 2, screen_height / 2)

  def update(self):
    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the player based on the pressed keys
    if keys[pygame.K_LEFT]:
      self.rect.x -= 5
    if keys[pygame.K_RIGHT]:
      self.rect.x += 5
    if keys[pygame.K_UP]:
      self.rect.y -= 5
    if keys[pygame.K_DOWN]:
      self.rect.y += 5

# Create a group of enemies
enemies = pygame.sprite.Group()

# Create an enemy object
class Enemy(pygame.sprite.Sprite):
  def _init_(self):
    super(Enemy, self)._init_()
    self.image = pygame.image.load("enemy.png")
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, screen_width)
    self.rect.y = random.randint(0, screen_height)

  def update(self):
    # Move the enemy towards the player
    self.rect.x += (player.rect.x - self.rect.x) / 100
    self.rect.y += (player.rect.y - self.rect.y) / 100

# Create the player object
player = Player()

# Add the player to the all_sprites group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create the clock object
clock = pygame.time.Clock()

# The game loop
running = True
while running:
  # Get the events that have happened since the last frame
  events = pygame.event.get()

  # Handle the events
  for event in events:
    if event.type == pygame.QUIT:
      running = False

  # Update the sprites
  all_sprites.update()

  # Check for collisions between the player and the enemies
  for enemy in enemies:
    if pygame.sprite.collide_rect(player, enemy):
      # The player has collided with an enemy, so end the game
      running = False

  # Fill the screen with white
  screen.fill((255, 255, 255))

  # Draw the sprites to the screen
  all_sprites.draw(screen)

  # Update the display
  pygame.display.flip()

  # Tick the clock
  clock.tick(60)

# Quit pygame
pygame.quit()
