# write code using tensorflow for a simple auto-encoder with training data random 4d vectors

import tensorflow as tf
import numpy as np

# Generate training data
num_samples = 1000
input_dim = 4
hidden_dim = 8
noise_factor = 0.1

x_train = np.random.rand(num_samples, input_dim)
x_train_noise = x_train + noise_factor * np.random.rand(*x_train.shape)

# Define the autoencoder model
inputs = tf.keras.Input(shape=(input_dim,))
encoded = tf.keras.layers.Dense(hidden_dim, activation='relu')(inputs)
decoded = tf.keras.layers.Dense(input_dim, activation='sigmoid')(encoded)

autoencoder = tf.keras.Model(inputs, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Train the autoencoder
autoencoder.fit(x_train_noise, x_train,
                epochs=1000,
                batch_size=32,
                shuffle=True)

# Test the autoencoder
x_test = np.random.rand(1, input_dim)
x_test_noise = x_test + noise_factor * np.random.rand(*x_test.shape)

decoded_x_test = autoencoder.predict(x_test)
decoded_x_test_noise = autoencoder.predict(x_test_noise)

print("Original input:", x_test)
print("Decoded output:", decoded_x_test)
print("Noisy input:", x_test_noise)
print("Decoded Noise output:", decoded_x_test_noise)
