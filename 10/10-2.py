import tensorflow as tf
with tf.Session() as sess:
    q = tf.FIFOQueue(1000,"float32")
    counter = tf.Variable(0.0)
    add_op = tf.assign_add(counter,tf.constant(1.0))
    enqueueData_op = q.enqueue(counter)

    qr = tf.train.QueueRunner(q,enqueue_ops=[add_op,enqueueData_op] * 2)
    sess.run(tf.initialize_all_variables())
    enqueue_threads = qr.cerate_threads(sess,taart = True) #启动入队线程

    for i in range(10):
        print(sess.run(q.dequeue()))