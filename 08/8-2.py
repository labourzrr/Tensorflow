import tensorflow as tf
input1 = tf.placeholder(tf.int32)
input2 = tf.placeholder(tf.int32)
sess = tf.Session()
output = tf.add(input1,input2)
print(sess.run(output,feed_dict = {input1:[4],input2:[6]}))


tf.cholesky(input,name= None)
tf.cholesky(input,name = None)
tf.cholesky(input,name = None)
tf.matrix_solve(matrix,rhs,adjoint = None,name = None)