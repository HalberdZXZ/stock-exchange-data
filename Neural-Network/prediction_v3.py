import os
import math
import numpy as np
import datetime as dt
import pandas as pd
from numpy import newaxis
from keras.layers import Dense, Activation, Dropout, LSTM
from keras.models import Sequential, load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint
import tensorflow as tf
import matplotlib.pyplot as plt





data = pd.read_csv('C:/Users/Halberdx/Documents/Python/Neural-Network/data/AXSUSDT.csv')

data.drop(['type'],  axis=1, inplace=True)

split = 0.85
i_split = int(len(data)*split)
cols = ['close', 'volume']
data_train = data.get(cols).values[:i_split]
data_test = data.get(cols).values[:i_split]
len_train = len(data_train)
len_test = len(data_test)
print(len(data), len_train, len_test)


secuenqu_lendth = 50; input_dim = 2; batch_size = 32; epoch = 2

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(100, input_shape=(secuenqu_lendth-1, input_dim),return_sequences=True),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.LSTM(100, return_sequences=True),
    tf.keras.layers.LSTM(100, return_sequences=False),
    tf.keras.layers.Dropout(.2),
    tf.keras.layers.Dense(1, activation='linear')
    ])

model.compile(optimizer='adam', loss='mse', metrics=[tf.keras.metrics.MeanAbsoluteError()])





# Формула: x=(x-min(x))/(max(x)-min(x))
def normalise( normalise, single_window=False): #by_prise_by_first_and_volume_by_middle
    normalised_data = []
    normalise = [normalise] if single_window else normalise
    for window in normalise:
        normalised_window = []
        for col_i in range(window.shape[1]):
            max_in_column = max(window[:, col_i])
            min_in_column = min(window[:, col_i])
            normalised_col = [((float(p) - float(min_in_column)) / (float(max_in_column) - float(min_in_column))) for p in window[:, col_i]]
            normalised_window.append(normalised_col)
        normalised_window = np.array(normalised_window).T
        normalised_data.append(normalised_window)
    return np.array(normalised_data)




def next_normalise( i, seq_len, normalise):
    window = data_train[i:i+seq_len]
    window = normalise(window, single_window=True)[0] if normalise else window
    x = window[:-1]
    y = window[-1, [0]]
    return x, y   



def get_train_data( seq_len, normalise):
    data_x = []
    data_y = []
    for i in range(len_train - seq_len + 1):
        x, y = next_normalise(i, seq_len, normalise)
        data_x.append(x)
        data_y.append(y)
    return np.array(data_x), np.array(data_y)

x, y = get_train_data( seq_len=50, normalise=True)


def get_train_data2(seq_len, normalise):
    data_windows = []
    for i in range(len_train - seq_len + 1):
        data_windows.append(data_train[i:i+seq_len])

    data_windows = np.array(data_windows).astype(float)
    data_windows = normalise(data_windows, single_window=False) if normalise else data_windows

    x = data_windows[:, :-1]
    y = data_windows[:, -1, [0]]
    return x,y

x2, y2 = get_train_data2( seq_len=50, normalise=True)

steps_per_epoch = math.ceil((len_train - 50) / 32)


callbacks = [
    EarlyStopping(monitor='val_loss', patience=2)
    ]
# callbacks = [
#     EarlyStopping(monitor='accuracy', patience=2)
#     ]

model.fit(x, y, epochs=epoch, batch_size=batch_size, callbacks=callbacks)




def get_test_data(seq_len, normalise):
    data_windows = []
    for i in range(len_test - seq_len + 1):
        data_windows.append(data_test[i:i+seq_len])

    data_windows = np.array(data_windows).astype(float)
    data_windows = normalise(data_windows, single_window=False) if normalise else data_windows

    x = data_windows[:, :-1]
    y = data_windows[:, -1, [0]]
    return x,y

x_test, y_test = get_test_data(seq_len=50, normalise=True)


model.evaluate(x_test, y_test, verbose=2)

def get_last_data( seq_len, normalise):
    last_data = data_test[seq_len:]
    data_windows = np.array(last_data).astype(float)
    #data_windows = np.array([data_windows])
    #data_windows = self.normalise(data_windows, single_window=False) if normalise else data_windows
    data_windows = normalise(data_windows, single_window=True) if normalise else data_windows
    return data_windows
    
last_data_2_predict_prices = get_last_data(-(50-1), False)
last_data_2_predict_prices_1st_price = last_data_2_predict_prices[0][0]
last_data_2_predict_prices_max = max(last_data_2_predict_prices[:, 0])
last_data_2_predict_prices_min = min(last_data_2_predict_prices[:, 0])

last_data_2_predict = get_last_data(-(50-1), True)

# print(-(50-1), last_data_2_predict.size)

# print(last_data_2_predict_prices)
# print(last_data_2_predict_prices_1st_price)
# print(last_data_2_predict)

predictions2 = model.predict(last_data_2_predict)
# print(predictions2, predictions2[0][0])

def next_normalise(price_1st, _data):
    return (_data + 1) * price_1st

# def next_normalise(price_max, price_min, _data):
#     return (_data*(price_max - price_min) + price_min)

predicted_price = next_normalise(last_data_2_predict_prices_1st_price, predictions2[0][0])
print(predicted_price)




