import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np


num_classes = 10


model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


x_train = np.random.random((100, 64, 64, 3))
y_train = np.random.randint(num_classes, size=(100,))


model.fit(x_train, y_train, epochs=10)


predictions = model.predict(x_train)

for i, x in enumerate(x_train):
    print(f"x: {x}, Predicted: {predictions[i]}, Actual: {y_train[i]}")
