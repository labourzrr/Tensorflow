import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.randn(100)
y_data = x_data * 0.3 + 0.15

weight = tf.Variable(0.5)
bias = tf.Variable(0.0)
x_ = tf.placeholder(tf.float32)
y_ = tf.placeholder(tf.float32)
y_model = x_ * weight + bias

loss = tf.pow((y_model - y_),2)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

for _ in range(10):
    for (x,y) in zip(x_data,y_data):
        sess.run(train_op,feed_dict = {x_:x,y_:y})
    print(weight.eval(sess),bias.eval(sess))

plt.plot(x_data,y_data,'ro',label = 'Original data')
plt.plot(x_data,x_data * weight.eval(sess)+ bias.eval(sess),label = 'Fitted line')
plt.legend()
plt.show()