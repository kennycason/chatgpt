# Here is some sample code for a simple particle simulation using Python and Pygame:
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This is a simple class that will help us draw the particles
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_x = random.randrange(-3, 3)
        self.speed_y = random.randrange(-3, 3)

    def update(self): # ChatGPT updated from move.
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # If the particle moves off the screen, put it back on
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed_x *= -1
        elif self.rect.x > 600:
            self.rect.x = 600
            self.speed_x *= -1

        if self.rect.y < 0:
            self.rect.y = 0
            self.speed_y *= -1
        elif self.rect.y > 400:
            self.rect.y = 400
            self.speed_y *= -1

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode([600, 400])

# Create a list of particles
particle_list = pygame.sprite.Group()

# Create 100 particles
for i in range(100):
    x = random.randrange(0, 600)
    y = random.randrange(0, 400)
    size = random.randrange(4, 8)
    particle = Particle(x, y, size)

    particle_list.add(particle)

# Main game loop
running = True
while running:
    # Check for any events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the particles
    particle_list.update()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the particles
    particle_list.draw(screen)

    # Update the screen
    pygame.display.flip()

pygame.quit()
