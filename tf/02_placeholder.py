import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

a = tf.placeholder(dtype=tf.float32, shape=[3])
b = tf.constant([5, 5, 5], dtype=tf.float32)
c = tf.add(a, b)


with tf.Session() as sess:
    writer = tf.summary.FileWriter('graphs/placeholders', sess.graph)
    print(sess.run(c, feed_dict={a: [1, 2, 3]}))
    writer.close()

# feed_dict with variables
a = tf.add(2, 3)
b = tf.multiply(a, 3)
x = tf.Variable(10)
y = tf.multiply(x, 3)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    print(sess.run(b))

    print(sess.run(b, feed_dict={a: 15}))
    sess.run(init)
    print(sess.run(y))
    print(sess.run(y, feed_dict={x: 20}))
