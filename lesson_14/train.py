#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:35:25 2022

This script shows how to log the training metrics to TensorBoard for a better
and more visual training monitoring. The Keras TensorBoard callback requires
TensorFlow, so we use a tiny custom callback built on the PyTorch SummaryWriter.

@author: janko
"""

import os
os.environ['KERAS_BACKEND'] = 'torch'    # has to be set before keras is imported

from datetime import datetime
import keras
from keras import Model
from keras.layers import Conv2D, Dense, Flatten, Input, MaxPooling2D
from torch.utils.tensorboard import SummaryWriter

keras.utils.set_random_seed(1234)


class TensorBoardLogger(keras.callbacks.Callback):
    """Writes all the metrics reported by Keras at the end of each epoch."""

    def __init__(self, log_dir):
        super().__init__()
        self.writer = SummaryWriter(log_dir)

    def on_epoch_end(self, epoch, logs=None):
        for name, value in logs.items():
            self.writer.add_scalar(name, value, epoch)

    def on_train_end(self, logs=None):
        self.writer.close()


# Create directory to store the TensorBoard logs
logdir = "logs/scalars/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoardLogger(logdir)

# Load data
(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Dataset params
num_classes = 10
size = x_train.shape[1]

# Normalization
x_train = x_train/255
x_test = x_test/255

# One-hot encoding
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print('Train set:   ', len(y_train), 'samples')
print('Test set:    ', len(y_test), 'samples')
print('Sample dims: ', x_train.shape)

# Build model
inputs = Input(shape=(size, size, 1))
net = Conv2D(16, kernel_size=(3, 3), activation="relu")(inputs)
net = MaxPooling2D(pool_size=(2, 2))(net)
net = Conv2D(16, kernel_size=(3, 3), activation="relu")(net)
net = MaxPooling2D(pool_size=(2, 2))(net)
net = Flatten()(net)
outputs = Dense(num_classes, activation="softmax")(net)

model = Model(inputs, outputs)
model.summary()

epochs = 100
batch_size = 128

# Register the TensorBoard callback and train
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,
                    callbacks=[tensorboard_callback])

# To open the TensorBoard monitor run
# $ tensorboard --logdir logs/scalars
# And then open localhost:6006 (or whatever port you have used)
