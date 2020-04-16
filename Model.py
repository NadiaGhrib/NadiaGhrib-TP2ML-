from ChargementDATA import *
from Preparation1 import *
from PreparationData import *
import pandas as pd
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
from keras.layers import Dropout

#On cherche à prédire Quelles catégories de produits les clients vont-ils acheter lors de leur prochain achat ?

#Le model :

model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(Y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')


#pb de multi-classe donc loss = cros_entropy et fonction d'activation = softmax

model.summary()
model.compile(loss='hinge', optimizer='sgd', metrics=['accuracy'])

callback_1 = keras.callbacks.TensorBoard(log_dir='trainings/t2')
callback_2 = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0.00005, patience=5)
callback_3 = keras.callbacks.ModelCheckpoint(filepath='weights.hdf5', verbose=1, save_best_only=True)

model.fit(x_train, y_train, epochs=50, batch_size=256, verbose=1, callbacks=[callback_1, callback_2, callback_3])

#evaluation
# Accuracy
accuracy = model.evaluate(x_test,y_test)
print(' Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accuracy[0],accr[1]))
