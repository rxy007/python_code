import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
import time
import utils
import matplotlib.pyplot as plt
DATA_FILE = 'data/birth_life_2010.txt'

data, n_samples = utils.read_birth_life_data(DATA_FILE)
dataset = tf.data.Dataset.from_tensor_slices((data[:, 0], data[:, 1]))
iterator = dataset.make_initializable_iterator()
X, Y = iterator.get_next()
w = tf.get_variable('w', initializer=tf.constant(0.0))
b = tf.get_variable('b', initializer=tf.constant(0.0))
Y_pred = X * w + b
loss = tf.square(Y - Y_pred)
optimizer = tf.train.GradientDescentOptimizer(0.001).minimize(loss)
start = time.time()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('graphs/linear_reg', sess.graph)
    for i in range(100):
        sess.run(iterator.initializer)
        total_loss = 0
        try:
            while True:
                _, l = sess.run([optimizer, loss])
                total_loss += l
        except tf.errors.OutOfRangeError:
            pass
        print('Epoch {0}: {1}'.format(i, total_loss/n_samples))
    writer.close()
    w_out, b_out = sess.run([w, b])
    print('w: %f, b: %f' %(w_out, b_out))
print('Took: %f seconds' %(time.time() - start))
plt.plot(data[:,0], data[:,1], 'bo', label='Real data')
plt.plot(data[:,0], data[:,0] * w_out + b_out, 'r', label='Predicted data with squared error')
# plt.plot(data[:,0], data[:,0] * (-5.883589) + 85.124306, 'g', label='Predicted data with Huber loss')
plt.legend()
plt.show()