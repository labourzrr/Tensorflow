import tensorflow as tf

matrix1 = tf.constant([[3.,5.]])
matrix2 = tf.constant([4,5])

sess = tf.Session()
print(matrix1)
print(sess.run(matrix1))
print("----------------------")
print(matrix2)
print(sess.run(matrix2))
