import tqdm
import os

import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split

from __init__ import IMG_HEIGHT, IMG_WIDTH


BUFFER_SIZE = 100
BATCH_SIZE = 1

image_name = []
index_arr = []

dir = os.listdir('./data/data')

def text_to_index(path):
    index = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(dir)):
        if dir[i] in path:
            index[i] = 1
            break

    return np.array(index)

def preprocess_image_train(image, y):
    image = resize_image(load(image))

    image = norm(image)

    return image, y


def dataset_creator():
    for i in tqdm.tqdm(dir):
        for dirname, _, filenames in os.walk(f'./data/data/{i}'):
            for filename in filenames:
                image = os.path.join(dirname, filename)

                image_name.append(image)

    for i in image_name:
        index_arr.append(text_to_index(i))

    X_train, X_test, y_train, y_test = train_test_split(image_name, index_arr)

    dataset_train = tf.data.Dataset.from_tensor_slices((X_train, y_train))

    dataset_test = tf.data.Dataset.from_tensor_slices((X_test, y_test))

    dataset_norm = lambda x: x.map(preprocess_image_train, num_parallel_calls=tf.data.AUTOTUNE)\
        .shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

    dataset_norm_2 = lambda x: x.map(preprocess_image_train, num_parallel_calls=tf.data.AUTOTUNE)\
        .shuffle(BUFFER_SIZE).batch(BATCH_SIZE)


    train_dataset = dataset_norm(dataset_train)
    test_dataset = dataset_norm_2(dataset_test)

    return train_dataset, test_dataset