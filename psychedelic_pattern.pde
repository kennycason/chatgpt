// Set the maximum number of iterations to generate the fractal
int maxIterations = 100;

// Set the initial zoom level
float zoom = 1.0;

// Set the size of the window
//size(500, 500);

void setup() {
  // Set the size of the window
  size(500, 500);
  // Set the background color to black
  background(0);
}

void draw() {
  // Increase the zoom level
  zoom *= 1.01;

  // Set the origin to the center of the window
  translate(width/2, height/2);

  // Set the stroke color to a random color
  stroke(random(255), random(255), random(255));

  // Begin drawing the fractal
  beginShape();
  for (int i = 0; i < maxIterations; i++) {
    // Calculate the angle of the current iteration
    float angle = TWO_PI * i / maxIterations;

    // Calculate the radius of the current iteration
    float radius = zoom * cos(4 * angle);

    // Calculate the x and y coordinates of the current iteration
    float x = radius * cos(angle);
    float y = radius * sin(angle);

    // Draw a line to the current iteration
    vertex(x, y);
  }
  endShape(CLOSE);
}
