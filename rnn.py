import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

timesteps = 10
features = 5

model = models.Sequential([
    layers.SimpleRNN(50, input_shape=(timesteps, features)),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

x_train = np.random.random((100, timesteps, features))
y_train = np.random.random((100, 1))


model.fit(x_train, y_train, epochs=10)


predictions = model.predict(x_train)

for i, x in enumerate(x_train):
    print(f"x: {x}, Predicted: {predictions[i]}, Actual: {y_train[i]}")
