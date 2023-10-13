from tensorflow import keras

from .dataset import dataset_creator
from .resnet import creator_model


model = creator_model()

def train():
    train_dataset, test_dataset = dataset_creator()

    loss_object = keras.losses.CategoricalCrossentropy()
    optimizer = keras.optimizers.Adam()

    model.compile(loss=loss_object, optimizer=optimizer, metrics=['acc'])

    model.summary()

    history = model.fit(train_dataset, epochs=1, validation_data=test_dataset)

    return history