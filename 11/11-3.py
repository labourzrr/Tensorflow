import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

thresholder = 1.0e-2
x1_data = np.random.randn(100).astype(np.float32)
x2_data = np.random.randn(100).astype(np.float32)
y_data = x1_data * 2 +x2_data *3 + 1.5

weight1 = tf.Variable(1.)
weight2 = tf.Variable(1.)
bias = tf.Variable(1.)
x1_ = tf.placeholder(tf.float32)
x2_ = tf.placeholder(tf.float32)
y_ = tf.placeholder(tf.float32)
y_model = tf.add(tf.multiply(x1_,weight1),tf.multiply(x2_,weight2),bias)


loss = tf.reduce_mean(tf.pow((y_model - y_),2))
train_op = tf.train.GradientDescentI