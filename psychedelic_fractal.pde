void setup() {
 // Set the size of the window
  size(500, 500);
  // Set the background color to black
  background(0);
  noStroke();
}

void draw() {
  // Set the fill color to a random color
  fill(random(255), random(255), random(255));

  // Calculate the size of the square
  float size = random(10, 50);

  // Calculate the x and y coordinates of the square
  float x = random(width - size);
  float y = random(height - size);

  // Draw the square
  rect(x, y, size, size);
}