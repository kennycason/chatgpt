/*
Using the programming language PROCESSING (java mode), write john conway's game of life and
then simplify the code and remove code comments
*/
float[][] hypercube = new float[][] {
  {-1, -1, -1, -1},
  {-1, -1, -1, 1},
  {-1, -1, 1, -1},
  {-1, -1, 1, 1},
  {-1, 1, -1, -1},
  {-1, 1, -1, 1},
  {-1, 1, 1, -1},
  {-1, 1, 1, 1}
};

int[][] edges = new int[][] {
  {0, 1}, {0, 2}, {0, 4}, {1, 3}, {1, 5}, {2, 3},
  {2, 6}, {3, 7}, {4, 5}, {4, 6}, {5, 7}, {6, 7},
  {0, 3}, {0, 5}, {1, 2}, {1, 6}, {2, 7}, {3, 4},
  {4, 7}, {5, 6}, {0, 7}, {1, 4}, {2, 5}, {3, 6}
};

void setup() {
 // size(500, 500);
  background(0);
  frameRate(10);
}


// This function will rotate the 4D hypercube around the X axis
void rotateX(float theta) {
  // Set the rotation matrix for the X axis
  float[][] rotationMatrix = new float[][] {
    {1, 0, 0, 0},
    {0, cos(theta), -sin(theta), 0},
    {0, sin(theta), cos(theta), 0},
    {0, 0, 0, 1}
  };

  // Apply the rotation matrix to each point of the hypercube
  for (int i = 0; i < 8; i++) {
    float[] point = hypercube[i];
    float[] rotatedPoint = new float[4];
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        rotatedPoint[j] += rotationMatrix[j][k] * point[k];
      }
    }
    hypercube[i] = rotatedPoint;
  }
}

// This function will rotate the 4D hypercube around the Y axis
void rotateY(float theta) {
  // Set the rotation matrix for the Y axis
  float[][] rotationMatrix = new float[][] {
    {cos(theta), 0, sin(theta), 0},
    {0, 1, 0, 0},
    {-sin(theta), 0, cos(theta), 0},
    {0, 0, 0, 1}
  };

  // Apply the rotation matrix to each point of the hypercube
  for (int i = 0; i < 8; i++) {
    float[] point = hypercube[i];
    float[] rotatedPoint = new float[4];
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        rotatedPoint[j] += rotationMatrix[j][k] * point[k];
      }
    }
    hypercube[i] = rotatedPoint;
  }
}

// This function will rotate the 4D hypercube around the Z axis
void rotateZ(float theta) {
  // Set the rotation matrix for the Z axis
  float[][] rotationMatrix = new float[][] {
    {cos(theta), -sin(theta), 0, 0},
    {sin(theta), cos(theta), 0, 0},
    {0, 0, 1, 0},
    {0, 0, 0, 1}
  };

  // Apply the rotation matrix to each point of the hypercube
  for (int i = 0; i < 8; i++) {
    float[] point = hypercube[i];
    float[] rotatedPoint = new float[4];
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        rotatedPoint[j] += rotationMatrix[j][k] * point[k];
      }
    }
    hypercube[i] = rotatedPoint;
  }
}

void rotateW(float theta) {
  // Set the rotation matrix for the W axis
  float[][] rotationMatrix = new float[][] {
    {cos(theta), 0, 0, -sin(theta)},
    {0, 1, 0, 0},
    {0, 0, 1, 0},
    {sin(theta), 0, 0, cos(theta)}
  };

  // Apply the rotation matrix to each point of the hypercube
  for (int i = 0; i < 8; i++) {
    float[] point = hypercube[i];
    float[] rotatedPoint = new float[4];
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 4; k++) {
        rotatedPoint[j] += rotationMatrix[j][k] * point[k];
      }
    }
    hypercube[i] = rotatedPoint;
  }
}

void draw() {
  // Clear the screen
  background(0);

  // Rotate the hypercube around the X, Y, Z, and W axes
  rotateX(frameCount * 0.01);
  rotateY(frameCount * 0.01);
  rotateZ(frameCount * 0.01);
  rotateW(frameCount * 0.01);

  // Draw the hypercube
  stroke(255);
  noFill();
  beginShape();
  for (int i = 0; i < edges.length; i++) {
    int[] edge = edges[i];
    float[] point1 = hypercube[edge[0]];
    float[] point2 = hypercube[edge[1]];
    vertex(point1[0], point1[1], point1[2], point1[3]);
    vertex(point2[0], point2[1], point2[2], point2[3]);
  }
  endShape();

  // Show the frame rate in the top-left corner of the screen
  fill(255);
  //text(format("FPS: %.1f", frameRate), 10, 20);
}
