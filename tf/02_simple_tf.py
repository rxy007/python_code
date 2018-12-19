import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

a = tf.constant(3, name='a')
b = tf.constant(2, name='b')
x = tf.add(a, b, name='add')
with tf.Session() as sess:
    writer = tf.summary.FileWriter('graphs/simple', sess.graph)
    print(sess.run(x))
    writer.close()

a = tf.constant([2, 2], name='a')
b = tf.constant([[0, 1], [2, 3]], name='b')
with tf.Session() as sess:
    print(sess.run(tf.div(b, a)))
    print(sess.run(tf.divide(b, a)))
    print(sess.run(tf.truediv(b, a)))
    print(sess.run(tf.floordiv(b, a)))
    print(sess.run(tf.truncatediv(b, a)))
    print(sess.run(tf.floor_div(b, a)))
    print(sess.run(tf.realdiv(5.0, 3.0)))# 只支持浮点类型的标量


a = tf.constant([10, 20], name='a')
b = tf.constant([2, 3], name='b')
with tf.Session() as sess:
    print(sess.run(tf.multiply(a, b)))
    print(sess.run(tf.tensordot(a, b, 0)))

t_0 = 19
x = tf.zeros_like(t_0, name='x')
y = tf.ones_like(t_0, name='y')

t_1 = ['apple', 'peach', 'banana']
x = tf.zeros_like(t_1)

t_2 = [[True, False, False],
       [False, False, True],
       [False, True, False]] 
x = tf.zeros_like(t_2) 
y = tf.ones_like(t_2) 

print(tf.int32.as_numpy_dtype)


my_const = tf.constant([1.0, 2.0], name='my_const')
print(tf.get_default_graph().as_graph_def())
