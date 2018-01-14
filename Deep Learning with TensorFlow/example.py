import tensorflow as tf

# node1 = tf.constant(3.0)  # tensorflow automatically changes constants to the proper value as needed (float, int, etc)
# node2 = tf.constant(4.0)
#
# # print(node1, node2)
#
# #what if we wanted to execute the graph?
# #call a session. Session puts the graph onto some hardware -- cpu/gpu and provides methods to execute the graphs
#
# # sess = tf.Session() #launches graph and creates a session obj
#
# # print(sess.run([node1, node2])) # remember to put this in a list
# #
# # sess.close()  # also have to free up memory by closing session
#
#
# # automatically closes session when done
# with tf.Session() as sess:
#     output = sess.run([node1, node2])
#     print(output)


#now let's see what happens when we want to execute some multiplication

#start by defining some constant nodes
#
# a = tf.constant(5.0)
# b = tf.constant(6.0)
#
# c = a*b
#
# with tf.Session() as sess:
#     output = sess.run(c)
#     file_writer = tf.summary.FileWriter('./graph', sess.graph)
#     print(output)
#
#
# #what if we want to see the progress of our graph? We'll use a Filewriter, and use "tensorboard --logdir=./"

# now what if we want to want to accept external input?

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
#
# adder_node = a + b
#
# with tf.Session() as sess:
#     file_writer = tf.summary.FileWriter('./graph', sess.graph)
#     output = sess.run(adder_node, {a: [1, 3], b: [2, 4]})
#     print(output)

#what are variables?

# W = tf.Variable([0.3], tf.float32)  # these will be changing weights, hence we use a variable
# b = tf.Variable([-0.3], tf.float32)  # these biases will also change
# x = tf.placeholder(tf.float32)  # this will be determined later
#
# linear_model = W * x + b
#
# # IMPORTANT: initialize all the variables
# init = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init)
#     output = sess.run(linear_model, {x: [1, 2, 3, 4]})
#     print(sess)

# how about the efficiency of our model?

# Model Parameters
W = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)

# Inputs and Outputs
x = tf.placeholder(tf.float32)  # input

linear_model = W * x + b

y = tf.placeholder(tf.float32)  # known output

# Loss function

squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)

# The model above isn't good because it has a high loss, so we should try to reduce it. We'll use an optimizer for it, ie gradient descent.

optimizer = tf.train.GradientDescentOptimizer(0.01)  # has the learning rate
train = optimizer.minimize(loss)  # computes and applies the gradients (can also be done in two sep steps, check documentation for more
                                    #https://www.tensorflow.org/api_docs/python/tf/train/GradientDescentOptimizer

init = tf.global_variables_initializer()

with tf.Session() as sess:
    output = sess.run(init)
    # print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
    for i in range(1000):
        sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})  # might wanna clear this up
    print(sess.run([W, b]))  # same with this
