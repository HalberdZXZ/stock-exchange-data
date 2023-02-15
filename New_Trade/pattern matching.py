import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None


NAME = 'KAVAUSDT'
data_new = pd.read_csv(fr'C:/Users/Halberdx/Documents/Python/New_Trade/{NAME}_NEW.csv')




describe_data = data_new.describe()
#выбоки пандас гугль

list_ind = []
for i in range(50000):
    list_ind.append(i)
ser0 = pd.DataFrame(columns=['type', 'interest', 'interest_series'], index=list_ind)
ser1 = pd.DataFrame(columns=['type', 'interest'], index=list_ind)
ser2 = pd.DataFrame(columns=['candle','shade_high','shade_low','interest', 'type'], index=list_ind)
ser3 = pd.DataFrame(columns=['candle','shade_high','shade_low','interest', 'type'], index=list_ind)

typ_ = data_new['type']
int_ = data_new['interest']  

 
#после 1 и 0    
'''i=0
list = []
while True:
    if data_new.type[i] == 0:
        list.append(data_new.type[i+1])
    i+=1
    if i == len(data_new):
        break


print(list.count(0), list.count(1))'''


'''#серии однитипных свечей плохой дисбаланс
i=0       
while True:     
    if data_new['type'][i] == 0:
        if data_new['type'][i+1] == 0:
            if data_new['type'][i+2] == 0:
                if  data_new['type'][i+3] == 0:
                    if  data_new['type'][i+4] == 0:
                        if  data_new['type'][i+5] == 0:
                            ser1['interest'][i+6] = data_new['interest'][i+6]
                            ser1['type'][i+6] = data_new['type'][i+6]
                            i+=5
    i+=1    
           
    if i == len(data_new)-5:
        break'''



'''#доджи
# после лонговой доджи плохой дисбаланс
i=0       
while True:     
    if (data_new['candle'][i]*3) < data_new['shade_low'][i] > (data_new['shade_high'][i] * 3):
        ser1['interest'][i+1] = data_new['interest'][i+1]
        ser1['type'][i+1] = data_new['type'][i+1]
    i+=1
    if i == len(data_new):
        break

# после шортовой доджи плохой дисбаланс
i=0       
while True:     
    if (data_new['candle'][i]*3) < data_new['shade_high'][i] > (data_new['shade_low'][i] * 3):
        ser1['interest'][i+1] = data_new['interest'][i+1]
        ser1['type'][i+1] = data_new['type'][i+1]
    i+=1
    if i == len(data_new):
        break'''  
    

'''#поглощение

# лонговое поглощение  плохой дисбаланс
i=0    
while True:
    sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4]      
    if sum_ < -1.5:
        if data_new['candle'][i+4] > 50 and data_new['type'][i+4] == 0:
            if data_new['candle'][i+5] > data_new['candle'][i+4] and data_new['type'][i+5] == 1:
                ser1['interest'][i+6] = data_new['interest'][i+6]
                ser1['type'][i+6] = data_new['type'][i+6]
                i+=5
    
    i+=1
            
    if i == len(data_new) - 6:
        break



# шортовое поглощение плохой дисбаланс
i=0    
while True:
    sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4]      
    if sum_ > 1.5:
        if data_new['candle'][i+4] > 50 and data_new['type'][i+4] == 1:
            if data_new['candle'][i+5] > data_new['candle'][i+4] and data_new['type'][i+5] == 0:
                ser1['interest'][i+6] = data_new['interest'][i+6]
                ser1['type'][i+6] = data_new['type'][i+6]
                i+=5
    
    i+=1
            
    if i == len(data_new) - 6:
        break'''

# просвет 



# #шортовый просвет плохой дисбаланс
# i=0      
# while True:
#       sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4] 
#       if sum_ > 2.4:
#           if data_new['candle'][i+4] > 100 and data_new['type'][i+4] == 1:
#               if data_new['candle'][i+4] > data_new['candle'][i+5] > 100 and data_new['type'][i+5] == 0:
#                   ser1['interest'][i+6] = data_new['interest'][i+6]
#                   ser1['type'][i+6] = data_new['type'][i+6]
#                   i+=5
#       i+=1            
#       if i == len(data_new) - 6: 
#           break

# #шортовый просвет плохой дисбаланс
# i=0      
# while True:
#       sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4] 
#       if sum_ < -2.4:
#           if data_new['candle'][i+4] > 100 and data_new['type'][i+4] == 0:
#               if data_new['candle'][i+4] > data_new['candle'][i+5] > 100 and data_new['type'][i+5] == 1:
#                   ser1['interest'][i+6] = data_new['interest'][i+6]
#                   ser1['type'][i+6] = data_new['type'][i+6]
#                   i+=5
#       i+=1            
#       if i == len(data_new) - 6: 
#           break


# двойной толчок

# шортовый двойной толчок плохой дисбаланс

# i=0       
# while True:
#       sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4] + int_[i+5]
#       if sum_ > 3.0:
#           if data_new['type'][i+5] == 1:
#               if (data_new['candle'][i+5] / 2) > data_new['candle'][i+6] and data_new['type'][i+6] == 0:
#                   if data_new['candle'][i + 7] > (data_new['candle'][i+5] / 2) and data_new['type'][i+7] == 0:
#                       ser1['interest'][i+8] = data_new['interest'][i+8]
#                       ser1['type'][i+8] = data_new['type'][i+8]
#                       i+=7
#       i+=1            
      
#       if i == len(data_new) - 8: 
#           break

# лонговый двойной толчок плохой дисбаланс

# i=0       
# while True:
#       sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4] + int_[i+5]
#       if sum_ < -3.0:
#           if data_new['type'][i+5] == 0:
#               if (data_new['candle'][i+5] / 2) > data_new['candle'][i+6] and data_new['type'][i+6] == 1:
#                   if data_new['candle'][i + 7] > (data_new['candle'][i+5] / 2) and data_new['type'][i+7] == 1:
#                       ser1['interest'][i+8] = data_new['interest'][i+8]
#                       ser1['type'][i+8] = data_new['type'][i+8]
#                       i+=7
#       i+=1            
      
#       if i == len(data_new) - 5: 
#           break       



#пинбар и повешенный следующая свеча а также следующие 5 свечей процент    

#пинбар на повышение неплохой дисбаланс, серия плохой дисбаланс
i=0       
while True:
      sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4]
      sum_1 = int_[i+6] + int_[i+7] + int_[i+8] + int_[i+9] + int_[i+10]
      if sum_ < -2.0:
          if (data_new['candle'][i+5] * 3) < data_new['shade_low'][i+5] > (data_new['shade_high'][i+5]*3):
                  ser0['interest'][i+6] = data_new['interest'][i+6]
                  ser0['type'][i+6] = data_new['type'][i+6]
                  ser0['interest_series'][i+6] = sum_1
                  i+=5
      i+=1            
      if i == len(data_new)-10: 
          break  


# #пинбар на понижение плохой дисбаланс, серия неплохой дисбаланс 
# i=0       
# while True:
#       sum_ = int_[i] + int_[i+1] + int_[i+2] + int_[i+3] + int_[i+4] 
#       sum_1 = int_[i+6] + int_[i+7] + int_[i+8] + int_[i+9] + int_[i+10]
#       if sum_ > 2.0:
#           if (data_new['candle'][i+5] * 3) < data_new['shade_high'][i+5] > (data_new['shade_low'][i+5]*3):
#                   ser0['interest'][i+6] = data_new['interest'][i+6]
#                   ser0['type'][i+6] = data_new['type'][i+6]
#                   ser0['interest_series'][i+6] = sum_1
#                   i+=5
#       i+=1            
#       if i == len(data_new)-10: 
#           break  



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
print('понижение:',  ser1_0['type'].count(), 'процент:', ser1_0['interest'].sum())








#посмотреть на график и поискать аналогии, посмотреть паттерны которые использует

ser1 = ser1.dropna()
ser1['interest'] = ser1['interest'].astype(float)
ser1['type'] = ser1['type'].astype(int)

# ser1 = ser1.reset_index(drop=True)


ser1_1 = ser1[ser1['type'] == 1]
ser1_0 = ser1[ser1['type'] == 0]




print('повышение:',  ser1_1['type'].count(), 'процент:', ser1_1['interest'].sum())
print('понижение:',  ser1_0['type'].count(), 'процент:', ser1_0['interest'].sum())

 #следующая проверка большое падение от 2% одной свечи что дальше и наоборот 
 #разделить этот файл на обработка данных и поиск закономерностей на 2 части

