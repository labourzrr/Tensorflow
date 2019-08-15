import tensorflow as tf
import numpy as np
inputX = np.random.rand(3000,1)
noise = np.random.normal(0,0.05,inputX.shape)
outputY = inputX * 4 + 1 + noise

#这是第一层
weight1 = tf.Variable(np.random.rand(inputX.shape[1],4))
bias1 = tf.Variable(np.random.rand(inputX.shape[1],4))
x1 = tf.placeholder(tf.float64,[None,1])
y1_ = tf.matmul(x1,weight1) + bias1
#这是第二层
weight2 = tf.Variable(np.random.rand(4,1))
bias2 = tf.Variable(np.random.rand(inputX.shape[1],1))
y2_ = tf.matmul(y1_,weight2) + bias2

y = tf.placeholder(tf.float64,[None,1])

loss = tf.reduce_mean(tf.reduce_sum(tf.square((y2_ - y)),reduction_indices=[1]))
train = tf.train.GradientDescentOptimizer(0.25).minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    sess.run(train,feed_dict={x1:inputX,y:outputY})

print("--------------weight1为：----------------")
print(weight1.eval(sess))
print("-----------------------------------------")
print("--------------weight2为：----------------")
print(weight2.eval(sess))
print("-----------------------------------------")
print("--------------bias1为：----------------")
print(bias1.eval(sess))
print("-----------------------------------------")
print("--------------bias2为：----------------")
print(bias2.eval(sess))
print("-----------------------------------------")

x_data = np.matrix([[1.],[2.],[3.]])
print(sess.run(y2_,feed_dict={x1:x_data}))