import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

s = tf.Variable(2, name='s')
m = tf.Variable([[0, 1], [2, 3]], name='m')
W = tf.Variable(tf.zeros([784, 10]), name='W')
v = tf.Variable(tf.truncated_normal([784, 10]), name='v')

s = tf.get_variable('s', initializer=tf.constant(2))
m = tf.get_variable('m', initializer=tf.constant([[0, 1], [2, 3]]))
W = tf.get_variable('W', shape=(784, 10), initializer=tf.zeros_initializer)
v = tf.get_variable('v', shape=(784, 10), initializer=tf.truncated_normal_initializer)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(v.eval())

w = tf.Variable(10)
w.assign(100)
with tf.Session() as sess:
    sess.run(w.initializer)
    print(sess.run(w))

w = tf.Variable(10)

ass_op = w.assign(100)
with tf.Session() as sess:
    sess.run(w.initializer)
    print(sess.run(ass_op))

a = tf.get_variable('s1', initializer=tf.constant(2))
a_times_two = a.assign(a * 2)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(a_times_two))
    print(sess.run(a_times_two))
    print(sess.run(a_times_two))

W = tf.Variable(10)
with tf.Session() as sess:
    sess.run(W.initializer)
    print(sess.run(W.assign_add(10)))     	# >> 20
    print(sess.run(W.assign_sub(2)))     	# >> 18

# Example 3: Each session has its own copy of variable
W = tf.Variable(10)
sess1 = tf.Session()
sess2 = tf.Session()
sess1.run(W.initializer)
sess2.run(W.initializer)
print(sess1.run(W.assign_add(10)))        	# >> 20
print(sess2.run(W.assign_sub(2)))        	# >> 8
print(sess1.run(W.assign_add(100)))        	# >> 120
print(sess2.run(W.assign_sub(50)))        	# >> -42
sess1.close()
sess2.close()

# Example 4: create a variable with the initial value depending on another variable
W = tf.Variable(tf.truncated_normal([700, 10]))
U = tf.Variable(W * 2)