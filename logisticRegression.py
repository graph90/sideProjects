import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

input_dim = 2

model = models.Sequential([
    layers.Dense(1, activation='sigmoid', input_shape=(input_dim,))
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

x_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y_train = np.array([0, 1, 1, 0], dtype=float)

model.fit(x_train, y_train, epochs=1000)

predictions = model.predict(x_train)

for i, x in enumerate(x_train):
    print(f"x: {x}, Predicted: {predictions[i][0]}, Actual: {y_train[i]}")
