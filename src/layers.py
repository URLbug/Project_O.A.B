import tensorflow as tf

from tensorflow.keras.layers import Conv2D, BatchNormalization


class Residual(tf.keras.layers.Layer):
  def __init__(self, filter_size, padding, strides, conv2d_plus=False, **kwargs):
    super(Residual, self).__init__(**kwargs)

    self.filter_size = filter_size
    self.padding = padding
    self.strides = strides
    self.conv2d_plus = conv2d_plus

    self.conv2d = Conv2D(filter_size ,kernel_size=1, padding=padding, strides=strides)
    self.conv2d_2 = Conv2D(filter_size ,kernel_size=1, padding=padding)
    self.batch_norm = BatchNormalization()
    self.batch_norm_2 = BatchNormalization()

    self.conv2d_3 = None

    if conv2d_plus:
      self.conv2d_3 = Conv2D(filter_size ,kernel_size=3, padding=padding, strides=strides)

    self.activation = tf.keras.layers.ReLU()
    self.activation_2 = tf.keras.layers.ReLU()

  def call(self, x):
    conv = self.activation(self.batch_norm(self.conv2d(x)))
    conv_2 = self.conv2d_2(conv)

    if self.conv2d_3 is not None:
      x = self.conv2d_3(x)

    y = self.batch_norm_2(conv_2)

    y += x

    return self.activation_2(y)

  def get_config(self):
    config = super(Residual, self).get_config()

    config['filter_size'] = self.filter_size
    config['padding'] = self.padding
    config['strides'] = self.strides
    config['conv2d_plus'] = self.conv2d_plus

    return config