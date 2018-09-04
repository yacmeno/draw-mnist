'''
Keras implementation of 'https://tensorflow.org/versions/r1.0/get_started/mnist/pros'
In addition, tensorboard is used + the model is saved for future use with tfjs
'''

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.initializers import Constant, TruncatedNormal
from keras.utils import to_categorical
from keras.callbacks import TensorBoard
import tensorflowjs as tfjs
import time #to append current time to model name

#load data
(x_train, y_train), (x_test, y_test) = mnist.load_data() 

#current shapes of x_train and x_test are (sample_size, width, height)
#keep the same shape, but specify that there's only 1 pixel dimension
#the 'channels_first' data format is adopted (argument of Flatten)
x_train = x_train.reshape(x_train.shape[0], 1, x_train.shape[1], x_train.shape[2])
x_test = x_test.reshape(x_test.shape[0], 1, x_test.shape[1], x_test.shape[2])

#change dtype to float32 and normalize pixel values between 0-1
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#represent y_train and y_test as vectors and not label value
#e.g. 3->[0, 0, 0, 1, 0, 0, 0, 0, 0, 0] (one-hot encoding)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

#tensorboard options
tensorboard = TensorBoard(
    log_dir='/full/path/to/logs/mnist-cnn-{}'.format(int(time.time())),
    histogram_freq=5,
    batch_size=50,
    write_graph=True,
    write_images=False
    )

#Building the CNN:
#kernel: stride of 1, zero padding to have same output size as input
#pooling: max pooling over 2x2 block
#Optimizer: ADAM to minimize categorical crossentropy

model = Sequential()
model.add(Conv2D(
    32,
    (5, 5),
    strides=(1, 1),
    padding='same',
    activation='relu',
    input_shape=(1, 28, 28),
    kernel_initializer=TruncatedNormal(stddev=0.1),
    bias_initializer=Constant(value=0.1)
    ))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1), padding='same'))
model.add(Conv2D(
    64,
    (5, 5),
    strides=(1, 1),
    padding='same',
    activation='relu',
    kernel_initializer=TruncatedNormal(stddev=0.1),
    bias_initializer=Constant(value=0.1)
    ))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1), padding='same'))
model.add(Flatten(data_format='channels_first'))
model.add(Dense(
    1024,
    activation='relu',
    kernel_initializer=TruncatedNormal(stddev=0.1),
    bias_initializer=Constant(value=0.1)
    ))
model.add(Dropout(0.5))
model.add(Dense(
    10,
    activation='softmax',
    kernel_initializer=TruncatedNormal(stddev=0.1),
    bias_initializer=Constant(value=0.1)
    ))
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
    )
model.fit(
    x_train, y_train,
    batch_size=50,
    epochs=100,
    validation_data=(x_test, y_test),
    verbose=1,
    callbacks=[tensorboard]
    )

#save model
#outputs weights as json + 2 binary weight files
tfjs.converters.save_keras_model(model, '/full/path/to/saved_model/')