import logging, os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#from keras.backend.tensorflow_backend import tf
import tensorflow as tf
logger = tf.get_logger()
logger.setLevel(logging.FATAL)

import keras
from keras import datasets, layers, models, activations, utils

# 모델 변수를 선언합니다.
model = models.Sequential()
# 모델에 첫번째 입력 레이어를 추가합니다.
model.add(layers.Conv2D(6, kernel_size=(5, 5), strides=(1, 1), activation='tanh', input_shape=(32, 32, 1)))

# 아래에 지시상항에 있는 모델 구조가 되도록 나머지 모델 구조를 선언해주세요.
model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(layers.Conv2D(16, kernel_size=(5, 5), strides=(1, 1), activation='tanh'))
model.add(layers.AveragePooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(layers.Conv2D(120, kernel_size=(5, 5), strides=(1, 1), activation='tanh'))
model.add(layers.Flatten())
model.add(layers.Dense(84, activation='tanh'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy, optimizer='SGD')

# Model 구조 확인
model.summary()