# Using python programming language write a mandelbrot zoom program in pygame
# I added code to only re-render the mandelbrot zoom or view settings have updated.
# brew install ImageMagick
# convert -delay 20 -loop 0 -duplicate 1,-2-1  mandelbrot1_*.png mandelbrot_zoom1.gif

import pygame
from pygame.locals import *
from time import sleep
from math import log

# Set the width and height of the screen
width = 600
height = 600

# Set the maximum number of iterations
max_iter = 100

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode([width, height])

# Set the initial values for the center of the screen and the zoom level
center_x = -0.5
center_y = 0
zoom = 1

# Create a function to calculate the color of a pixel
def calculate_color(c_real, c_imag):
    # Set the initial values for the real and imaginary parts of the complex number
    z_real = 0
    z_imag = 0

    # Iterate until the maximum number of iterations is reached or the complex number escapes
    for i in range(max_iter):
        z_real, z_imag = z_real**2 - z_imag**2 + c_real, 2*z_real*z_imag + c_imag

        # If the complex number escapes, return a value based on the number of iterations
        if z_real**2 + z_imag**2 > 4:
            return (255*i)//max_iter

    # If the complex number does not escape, return black
    return 0, 0, 0

# Create a function to draw the Mandelbrot set
def draw_mandelbrot():
    # Calculate the width and height of each pixel
    pixel_width = 2/width/zoom
    pixel_height = 2/height/zoom

    # Iterate over each pixel in the screen
    for x in range(width):
        for y in range(height):
            # Calculate the real and imaginary parts of the complex number corresponding to the pixel
            c_real = center_x + (x - width/2)*pixel_width
            c_imag = center_y + (y - height/2)*pixel_height

            # Calculate the color of the pixel and draw it on the screen
            color = calculate_color(c_real, c_imag)
            screen.set_at((x, y), color)

# Main loop
needRender = True
running = True
while running:
    # Draw the Mandelbrot set on the screen
    if needRender:
        draw_mandelbrot()
        pygame.display.flip()
        needRender = False

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            needRender = True
            # Zoom in or out when the + or - keys are pressed
            if event.key == K_PLUS:
                zoom *= 2
            elif event.key == K_MINUS:
                zoom /= 2
            # Move the center of the screen when the arrow keys are pressed
            elif event.key == K_UP:
                center_y += 1/zoom
            elif event.key == K_DOWN:
                center_y -= 1/zoom
            elif event.key == K_LEFT:
                center_x -= 1/zoom
            elif event.key == K_RIGHT:
                center_x += 1/zoom
        elif event.type == MOUSEBUTTONDOWN:
            needRender = True
            # Get the current position of the mouse cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calculate the width and height of each pixel
            pixel_width = 2/width/zoom
            pixel_height = 2/height/zoom

            # Adjust the center of the screen based on the movement of the mouse cursor
            center_x += (mouse_x - width/2)*pixel_width
            center_y += (mouse_y - height/2)*pixel_height

            # Zoom in or out based on the mouse button being pressed
            if pygame.mouse.get_pressed()[0]:
                zoom *= 2
            elif pygame.mouse.get_pressed()[2]:
                zoom /= 2

# Clean up
pygame.quit()
