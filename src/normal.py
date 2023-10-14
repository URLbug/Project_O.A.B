import tensorflow as tf

from __init__ import IMG_HEIGHT, IMG_WIDTH


def resize_image(img):
    img = tf.image.resize(
        img, (IMG_WIDTH, IMG_HEIGHT), method=tf.image.ResizeMethod.NEAREST_NEIGHBOR
    )

    return img

def load(image_file):
  image = tf.io.read_file(image_file)
  image = tf.io.decode_jpeg(image)

  input_image = tf.cast(image, tf.float32)

  return input_image

def norm(img):
    img = tf.cast(img, tf.float32)

    img = (img / 127.5) - 1

    return img