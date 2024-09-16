import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

model = models.Sequential([
    layers.Dense(1, input_shape=(1,))
])

model.compile(optimizer='sgd', loss='mean_squared_error')

x_train = np.array([1, 2, 3, 4], dtype=float)
y_train = np.array([1, 3, 5, 7], dtype=float)

model.fit(x_train, y_train, epochs=1000, verbose=0)

predictions = model.predict(x_train)

for i, x in enumerate(x_train):
    print(f"x: {x}, Predicted: {predictions[i][0]}, Actual: {y_train[i]}")
