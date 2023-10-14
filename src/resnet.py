import tensorflow as tf

from tensorflow import keras 

from __init__ import dirs, IMG_WIDTH, IMG_HEIGHT
from .layers import Residual
from .normal import resize_image, norm, load


def creator_model(
    filter=128, padding='same', strides=1, kernel_size=3, dropout=.2):
    
    model = keras.Sequential([
        keras.layers.Input((IMG_HEIGHT, IMG_WIDTH, 3)),
        keras.layers.Conv2D(filter, padding=padding, strides=strides+1, kernel_size=7),
        keras.layers.MaxPool2D(strides=strides+1),
        Residual(filter, padding, strides),
        Residual(filter, padding, strides),

        keras.layers.Dropout(dropout),

        Residual(filter*2, padding, strides+1, True),
        Residual(filter*2, padding, strides),

        keras.layers.Dropout(dropout),

        Residual(filter*4, padding, strides+1, True),
        Residual(filter*4, padding, strides),

        keras.layers.Dropout(dropout),

        Residual(filter*8, padding, strides+1, True),
        Residual(filter*8, padding, strides),

        keras.layers.Dropout(dropout),

        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dropout(dropout),
        keras.layers.Flatten(),
        keras.layers.Dense(len(dirs), activation='softmax')
    ])

    return model

def resnet_ark(image, model):
    image = resize_image(load(image))

    image = norm(image)

    index = dirs[
        model(
            tf.reshape(image, [1, 64, 64, 3])
            ).numpy().argmax()
        ]
    
    return index

def evalute(image, real, model):
    image = resize_image(load(image))

    image = norm(image)

    evalute = model.evaluate(
            tf.reshape(image, [1, 64, 64, 3])
            )
    
    return evalute