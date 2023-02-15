from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
pd.options.mode.chained_assignment = None
import datetime


api_key = '*********'
api_secret = '********'
client = Client(api_key, api_secret)

NAME = 'KAVAUSDT'

data = client.futures_historical_klines(NAME, Client.KLINE_INTERVAL_30MINUTE, "2020-05-15", "today")

data = pd.DataFrame(data, columns=['datetime', 'open', 'high', 'low', 'close', 'volume', '1', '2', '3', '4', '5', '6'])
data.drop(labels = [len(data)-1], inplace=True)
data = data.drop(columns=['datetime', '1', '2', '3', '4', '5', '6'])


#делается для удобства в дальнейшем в обработке данных
data.open = data.open.astype(str)
data.open = data.open.str.replace('[.]','',regex=True)

data.high = data.high.astype(str)
data.high = data.high.str.replace('[.]','',regex=True)

data.low = data.low.astype(str)
data.low = data.low.str.replace('[.]','',regex=True)

data.close = data.close.astype(str)
data.close = data.close.str.replace('[.]','',regex=True)

data.volume = data.volume.astype(str)
data.volume = data.volume.str.replace('[.]','',regex=True)





data[['open', 'high', 'low', 'close', 'volume']] = data[['open', 'high', 'low', 'close', 'volume']].astype(float)

# формирование бинарного столбца 'вверх или вниз' 1 = лонговая свеча 0 = шортовая свеча
data['type'] = data['close']
i=0
l=1
for f in range((len(data)-1)):
    if data['close'][i] < data['close'][l]:
        data['type'][l] = 1
    else:
        data['type'][l] = 0
    i+=1
    l+=1

#Формирования столбца показывающий процент
data['interest'] = 0
a=1
b=0
for f in range((len(data)-1)):
    if data['close'][a] > data['close'][b]:
        data['interest'][a] = data['close'][a] / data['close'][b]
        data['interest'][a] = 100 - (100 / data['interest'][a])
    else:
        data['interest'][a] = data['close'][b] / data['close'][a]
        data['interest'][a] = 100 - (100 / data['interest'][a])
    a+=1
    b+=1

data.drop(labels = [0],axis = 0, inplace=True)
data.to_csv(fr"C:/Users/Halberdx/Documents/Python/New_Trade/{NAME}.csv", index=False)
