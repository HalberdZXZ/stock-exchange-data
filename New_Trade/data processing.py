import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None


NAME = 'KAVAUSDT'
data = pd.read_csv(fr'C:/Users/Halberdx/Documents/Python/New_Trade/{NAME}.csv')

#Основа корректировки датафрейма(в дальнейшем нужно дополнить)
data_new = pd.DataFrame(columns=['candle','shade_high','shade_low','interest', 'type'])
data_new['interest'] = data['interest']
data_new['type'] = data['type']

# для визуализации и более удобной работы 
# условно:
# тело свечи = close - open
# верхняя тень свечи(если закрытие было шортовым) = high - open 
i=0
while True:
    if data['open'][i] < data['close'][i]:
        data_new['candle'][i] = data['close'][i] - data['open'][i]
        
    if data['open'][i] >= data['close'][i]:
        data_new['candle'][i] = data['open'][i] - data['close'][i] 
        
    i+=1
    if i == len(data_new):
        break

i=0
while True:
    if data['open'][i] >= data['close'][i]:
    
        if data['open'][i] < data['high'][i]:
            data_new['shade_high'][i] = data['high'][i] - data['open'][i]
        
        if data['open'][i] >= data['high'][i]:
            data_new['shade_high'][i] = data['open'][i] - data['high'][i] 
    
    if data['open'][i] <= data['close'][i]:   
        
        if data['close'][i] < data['high'][i]:
            data_new['shade_high'][i] = data['high'][i] - data['close'][i]
      
        if data['high'][i] >= data['close'][i]:
            data_new['shade_high'][i] = data['high'][i] -  data['close'][i]    
        
    i+=1
    if i == len(data_new):
        break   
    
i=0
while True:
    if data['open'][i] <= data['close'][i]:
    
        if data['open'][i] < data['low'][i]:
            data_new['shade_low'][i] = data['low'][i] - data['open'][i]
        
        if data['open'][i] >= data['low'][i]:
            data_new['shade_low'][i] = data['open'][i] - data['low'][i] 
    
    if data['open'][i] >= data['close'][i]:   
        
        if data['close'][i] > data['low'][i]:
            data_new['shade_low'][i] = data['close'][i] -  data['low'][i]
      
        if data['low'][i] >= data['close'][i]:
            data_new['shade_low'][i] = data['low'][i] -  data['close'][i]  
        
    i+=1
    if i == len(data_new):
        break  

data_new[['shade_high', 'shade_low', 'candle', 'type']] = data_new[['shade_high', 'shade_low', 'candle', 'type']].astype(int)    
data_new['interest'] = data_new['interest'].astype(float)

#присвоение '-' процентам где движение было шортовым чтобы в дальнейшем более проще делать математические операции
i=0
while True:
    d = data_new['interest'][i]
    if data_new['type'][i] == 0:
        data_new['interest'][i] = data_new.at[i, 'interest'] = -d
    i+=1
    if i == len(data_new):
        break
        

data_new.to_csv(fr"C:/Users/Halberdx/Documents/Python/New_Trade/{NAME}_NEW.csv", index=False)