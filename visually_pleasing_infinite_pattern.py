# Using the python programming language that please write a program for visually pleasing infinite psychedelic pattern.

# video: https://v.usetapes.com/lhoOLUoir8
# npm install turtle
# brew install python-tk

import turtle

# Set the background color to black
turtle.bgcolor("black")

# Set the turtle speed to the maximum possible
turtle.speed(0)

# Create a list of colors to use in the pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Use a for loop to repeat the pattern
for i in range(360):
  turtle.pencolor(colors[i % 6])  # Use the next color in the list
  turtle.width(i / 100 + 1)  # Increase the pen width as the pattern progresses
  turtle.forward(i)  # Move forward
  turtle.left(59)  # Turn left

# Keep the window open until it is closed by the user
turtle.mainloop()
