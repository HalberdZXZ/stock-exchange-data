

import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None
import math
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import re

from tensorflow.keras.layers import Dense, LSTM, Input, Dropout, Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer, text_to_word_sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences


NAME = 'KAVAUSDT'
data_new = pd.read_csv(fr'C:/Users/Halberdx/Documents/Python/data analysis/{NAME}_NEW.csv')


#Обобщение данных мы хотим обобщить свечи так чтобы они чаще повторялись и можно было выделить определенный тип 
# свечи будут представлены так(тут никакой математики важен порядок в нейройнную сеть они будут подаваться по индексу) 203050-3  - первые 3 числа процентное соотношение теней и тела свечи, далее тип свечи и ее сила(процент условно) 

i=0
for _ in range(len(data_new)):
    sum_int = data_new['candle'][i] + data_new['shade_high'][i] + data_new['shade_low'][i]
    data_new['candle'][i] = 100 / (sum_int / data_new['candle'][i])
    data_new['shade_high'][i] = 100 / (sum_int / data_new['shade_high'][i])
    data_new['shade_low'][i] = 100 / (sum_int / data_new['shade_low'][i])
    i+=1
    
data_new['candle'] = data_new['candle'].round(-1)
data_new['shade_high'] = data_new['shade_high'].round(-1)
data_new['shade_low'] = data_new['shade_low'].round(-1)

data_new['interest'] = data_new['interest'].round().astype(int)


data_new = data_new.astype(str)
data_new['candle'] = data_new['candle'].str.replace('[.]0','',regex=True)
data_new['shade_high'] = data_new['shade_high'].str.replace('[.]0','',regex=True)
data_new['shade_low'] = data_new['shade_low'].str.replace('[.]0','',regex=True)


data_new['type'] = data_new['type'].astype(int)

data_new['candle_full'] = data_new['candle'] + data_new['shade_high'] + data_new['shade_low'] + data_new['interest'] 

data_new.drop(columns =['candle', 'shade_high', 'shade_low', 'interest'], axis=1, inplace=True)








#разделение данных на шорт и лонг  изначально попробуем  с 20 свечами и 20 смещением
i1 = 0
i2 = 20

list_0 = []
list_1 = []
while True:
    if data_new['type'][i2] == 0:
        
        list_0.append(' '.join(data_new['candle_full'][i1:i2].tolist()))
            
            
    if data_new['type'][i2] == 1:
         
        list_1.append(' '.join(data_new['candle_full'][i1:i2].tolist()))
            
            
    i1+=20
    i2+=20
    
    if i2 > len(data_new) :
        break


  


full_list = list_1 + list_0
count_true = len(list_1)
count_false = len(list_0)
total_lines = count_true + count_false
print(count_true, count_false, total_lines)


maxWordsCount = 1000
tokenizer = Tokenizer(num_words=maxWordsCount, filters='!–"—#$%&amp;()*+,/:;<=>?@[\\]^_`{|}~\t\n\r«»', lower=True, split=' ', char_level=False)
tokenizer.fit_on_texts(full_list)

dist = list(tokenizer.word_counts.items())
print(dist[:10])
print(full_list[0][:100])


max_number_len = 20
data = tokenizer.texts_to_sequences(full_list) 
data_pad = pad_sequences(data, maxlen=max_number_len)
print(data_pad)

print( list(tokenizer.word_index.items()) )


X = data_pad
Y = np.array([[0, 1]]*count_true + [[1, 0]]*count_false)
print(X.shape, Y.shape)

indeces = np.random.choice(X.shape[0], size=X.shape[0], replace=False)
X = X[indeces]
Y = Y[indeces]


model = Sequential()
model.add(Embedding(maxWordsCount, 128, input_length = max_number_len))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(64))
model.add(Dense(2, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=Adam(0.0001))

history = model.fit(X, Y, batch_size=32, epochs=50)

reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

def sequence_to_text(list_of_indices):
    words = [reverse_word_map.get(letter) for letter in list_of_indices]
    return(words)

numbers = list_1[5]
data = tokenizer.texts_to_sequences([numbers])
data_pad = pad_sequences(data, maxlen=max_number_len)
print( sequence_to_text(data[0]) )

res = model.predict(data_pad)
print(res, np.argmax(res), sep='\n')
    