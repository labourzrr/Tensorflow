import tensorflow as tf

a = tf.constant([[1,2],[3,4]])

sess = tf.Session()

print(a)
print(sess.run(a))

matrix1 = tf.placeholder('float',[2,2])
a = sess.run(a)
matrix2 = sess.run(matrix1,feed_dict = {matrix1:a})
print(matrix2)