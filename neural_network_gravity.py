# Input: Write a neural network to calculate the force of gravity between various planets within our solar system
# Follow up: Rewrite the above program to use real values for planet masses and distance

import numpy as np
from keras.layers import Dense
from keras.models import Sequential

# Define the input values: mass1, mass2, distance
# The masses are in kilograms, and the distances are in meters
input_values = np.array([[1.9891e30, 5.9736e24, 149.6e9],  # Earth-Sun
                         [1.9891e30, 7.3477e22, 238.9e9],  # Moon-Sun
                         [1.9891e30, 1.8986e27, 778.3e9],  # Jupiter-Sun
                         [5.9736e24, 7.3477e22, 3.844e8],  # Moon-Earth
                         [5.9736e24, 1.8986e27, 778.3e9],  # Jupiter-Earth
                         [7.3477e22, 1.8986e27, 816.6e9]]) # Jupiter-Moon

# Define the target values: force of gravity
# The forces are in newtons
target_values = np.array([[3.5269e22],  # Earth-Sun
                          [2.0585e20],  # Moon-Sun
                          [1.0473e28],  # Jupiter-Sun
                          [1.9838e20],  # Moon-Earth
                          [1.0309e28],  # Jupiter-Earth
                          [1.9128e20]]) # Jupiter-Moon

# Create the model
model = Sequential()
model.add(Dense(20, input_dim=3, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mse', optimizer='adam')

# Fit the model on the input and target values
model.fit(input_values, target_values, epochs=100, verbose=0)

# Make predictions on the input values
predictions = model.predict(input_values)

# Print the predictions
print(predictions)

# first errored output
# the above code prints [[nan] [nan] [nan] [nan]] instead of actual numbers