import tensorflow as tf
matrix1 = tf.constant([[3.,3.]])
matrix2 = tf.constant([3.,3.])
sess = tf.Session()


matrix = tf.add(matrix2,matrix1)
print(matrix)
print(sess.run(matrix))

