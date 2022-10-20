import tensorflow as tf
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

l0 = Dense(units=1, input_shape=[1])
model = Sequential([l0])
model.compile(optimizer='sgd', loss='mean_squared_error')

#xs = np.array([-3, -2, -1, 0, 1, 2, 3], dtype=float)
#ys = np.array([9, 4, 1, 0, 1, 4, 9], dtype=float)
xs = np.array([0, 1, 2, 3], dtype=float)
ys = np.array([300, 309, 318, 327], dtype=float)

model.fit(xs, ys, epochs=2000)

print(model.predict([4]))
print("l0 learnt = {}".format(l0.get_weights()))
