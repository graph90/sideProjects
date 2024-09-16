import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

input_dim = 10

model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(input_dim,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


x_train = np.random.random((100, input_dim))
y_train = np.random.randint(2, size=(100, 1))

model.fit(x_train, y_train, epochs=10)

predictions = model.predict(x_train)

for i, x in enumerate(x_train):
    print(f"x: {x}, Predicted: {predictions[i][0]}, Actual: {y_train[i][0]}")
