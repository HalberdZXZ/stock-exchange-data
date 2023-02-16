import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None


data_new = pd.read_csv('C:/Users/Halberdx/Documents/Python/data analysis/data_new.csv')








'''#что было до сильного роста или падения

i=2      
while True:
    if data_new['interest'][i] < -1.5 and data_new['type'][i] == 0:
        
        ser2.iloc[i-3] = data_new.iloc[i-3]
        ser2.iloc[i-2] = data_new.iloc[i-2]
        ser2.iloc[i-1] = data_new.iloc[i-1]
        i+=2
    i+=1
    if i == len(data_new):
        break






ser2 = ser2.dropna()
ser2[['candle','shade_high','shade_low','type']] = ser2[['candle','shade_high','shade_low', 'type']].astype(int)
ser2['interest'] = ser2['interest'].astype(float)

ser2 = ser2.reset_index(drop=True)


#из что было до сильного падения где 3 свечи мы берем последнию задаем еще условие и вписываем в новый датафрейм
# i=2 
# for _ in range(2,len(ser2),3):
#     # if ser2['candle'][i] > 200:
#     ser3.iloc[i] = ser2.iloc[i]
        
        
#     i+=3            


# ser3 = ser3.dropna()
# ser3[['candle','shade_high','shade_low','type']] = ser2[['candle','shade_high','shade_low', 'type']].astype(int)
# ser3['interest'] = ser2['interest'].astype(float)







#счетчики определенных 3 свечей на их повторение в ser2(выборке) и data_new

i=0  
count_ser2 = 0     
while True:
    if ser2['candle'][i] < ser2['candle'][i+1] > ser2['candle'][i+2]:
        if ser2['type'][i] == 1 and ser2['type'][i+1] == 0  and ser2['type'][i+2] == 1:
            count_ser2+=1
            i+=2 
    i+=1
    if i == len(ser2)-2:
        break
    
i=0  
count_data_new = 0     
while True:
    if data_new['candle'][i] < data_new['candle'][i+1] > data_new['candle'][i+2]:
        if data_new['type'][i] == 1 and data_new['type'][i+1] == 0 and data_new['type'][i+2] == 1:
            count_data_new+=1
            i+=2 
    i+=1
    if i == len(data_new)-3:
        break
 
#проверка комбинаций свечей которые мы получили из что было до сильного падения или роста и проверили на определнные свечи
i=0     
while True:
    if data_new['candle'][i] < data_new['candle'][i+1] > data_new['candle'][i+2]:
        if data_new['type'][i] == 1 and data_new['type'][i+1] == 0 and data_new['type'][i+2] == 1:
            ser1['interest'][i+3] = data_new['interest'][i+3]
            ser1['type'][i+3] = data_new['type'][i+3]
           
            i+=2 
    i+=1
    if i == len(data_new)-3:
        break'''
        
        
'''#пинбар и повешенный следующая свеча а также следующие 5 свечей процент         
# #повешенный на повышение плохой дисбаланс, серия плохой дисбаланс
# i=0       
# while True:
#       sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4]
#       sum_1 = int_[i+6] + int_[i+7] + int_[i+8] + int_[i+9] + int_[i+10]
#       if sum_ < -2.0:
#           if (data_new['candle'][i+5] * 3) < data_new['shade_high'][i+5] > (data_new['shade_low'][i+5]*3):
#                   ser0['interest'][i+6] = data_new['interest'][i+6]
#                   ser0['type'][i+6] = data_new['type'][i+6]
#                   ser0['interest_series'][i+6] = sum_1
#                   i+=5
#       i+=1            
#       if i == len(data_new)-10: 
#           break  

#повешенный на понижение хороший дисбаланс, серия плохой дисбаланс
i=0       
while True:
      sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4] 
      sum_1 = int_[i+6] + int_[i+7] + int_[i+8] + int_[i+9] + int_[i+10]
      if sum_ > 2.0:
          if (data_new['candle'][i+5] * 3) < data_new['shade_low'][i+5] > (data_new['shade_high'][i+5]*3):
                  ser0['interest'][i+6] = data_new['interest'][i+6]
                  ser0['type'][i+6] = data_new['type'][i+6]
                  ser0['interest_series'][i+6] = sum_1
                  i+=5
      i+=1            
      if i == len(data_new)-10: 
          break







ser0 = ser0.dropna()
ser0['interest'] = ser0['interest'].astype(float)
ser0['type'] = ser0['type'].astype(int)
ser0['interest_series'] = ser0['interest_series'].astype(float)

ser0 = ser0.reset_index(drop=True)

ser0_0 = ser0[ser0['interest_series'] > 0]
ser0_1 = ser0[ser0['interest_series'] < 0]

ser1_1 = ser0[ser0['type'] == 1]
ser1_0 = ser0[ser0['type'] == 0]



print('Рост:', ser0_0['interest_series'].count(), 'Процент:', ser0_0['interest_series'].sum())
print('Падение:', ser0_1['interest_series'].count(), 'Процент:', ser0_1['interest_series'].sum())
print('повышение:',  ser1_1['type'].count(), 'процент:', ser1_1['interest'].sum())
print('понижение:',  ser1_0['type'].count(), 'процент:', ser1_0['interest'].sum())'''       
