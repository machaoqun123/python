import tensorflow as tf
from tensorflow.keras import datasets, layers, optimizers, Sequential, metrics

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.random.set_seed(2345)

convLayers = [
    # unit 1
    layers.Conv2D(64, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.Conv2D(64, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    # unit 2
    layers.Conv2D(128, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.Conv2D(128, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    # unit 3
    layers.Conv2D(256, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.Conv2D(256, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    # unit 4
    layers.Conv2D(512, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.Conv2D(512, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same'),

    # unit 5
    layers.Conv2D(512, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.Conv2D(512, kernel_size=[3, 3], padding='same', activation=tf.nn.relu),
    layers.MaxPool2D(pool_size=[2, 2], strides=2, padding='same')

]


def preprocess(x, y):
    """
    x is a simple image, not a batch
    """
    x = tf.cast(x, dtype=tf.float32) / 255.
    y = tf.cast(y, dtype=tf.int32)
    return x, y


(x, y), (xTest, yTest) = datasets.cifar100.load_data()
y = tf.squeeze(y, axis=1)
yTest = tf.squeeze(yTest, axis=1)
print(x.shape, y.shape, xTest.shape, yTest.shape)

trainDB = tf.data.Dataset.from_tensor_slices((x, y))
trainDB = trainDB.shuffle(1000).map(preprocess).batch(batch_size=64)

testDB = tf.data.Dataset.from_tensor_slices((xTest, yTest))
testDB = testDB.map(preprocess).batch(batch_size=64)

# def main():
# [b, 32, 32, 3] => [b, 1, 1, 512]
convNet = Sequential(convLayers)
# x = tf.random.normal([4, 32, 32, 3])
# out = convNet(x)
# print(out.shape)

fcNet = Sequential([
    layers.Dense(256, activation=tf.nn.relu),
    layers.Dense(128, activation=tf.nn.relu),
    layers.Dense(100, activation=None),
])

convNet.build(input_shape=[None, 32, 32, 3])
fcNet.build(input_shape=[None, 512])
optimizer = optimizers.Adam(learning_rate=1e-4)

variables = convNet.trainable_variables + fcNet.trainable_variables

for epoch in range(50):
    for step, (x, y) in enumerate(trainDB):
        with tf.GradientTape() as tape:
            out = convNet(x)
            out = tf.reshape(out, [-1, 512])
            logits = fcNet(out)

            yOnehot = tf.one_hot(y, depth=100)
            loss = tf.losses.categorical_crossentropy(yOnehot, logits, from_logits=True)
            loss = tf.reduce_mean(loss)

        grads = tape.gradient(loss, variables)
        optimizer.apply_gradients(zip(grads, variables))

        if step % 100 == 0:
            print(epoch, step, 'loss:', float(loss))