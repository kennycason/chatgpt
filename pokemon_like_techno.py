import pygame
import random

# Initialize the pygame module
pygame.init()

# Set the tempo (beats per minute)
tempo = 180

# Set the duration of each note (in seconds)
duration = 60 / tempo

# Set the list of notes to use in the pattern
notes = [
    pygame.mixer.Sound("sounds/Alesis-Fusion-Acoustic-Bass-C2.wav"),
    pygame.mixer.Sound("sounds/Alesis-Fusion-Bass-C3.wav"),
    pygame.mixer.Sound("sounds/Alesis-Sanctuary-QCard-AcoustcBas-C2.wav"),
    # pygame.mixer.Sound("sounds/Alesis-Fusion-Viola-C5.wav"),
    pygame.mixer.Sound("sounds/Bamboo.wav"),
]

# Create a pattern using the list of notes
pattern = [random.choice(notes) for _ in range(128)]

# Play the pattern
for note in pattern:
    note.play()
    pygame.time.wait(int(duration * 1000))

# Keep the program running until the user closes the window
while True:
    pass