import pandas as pd
dataset = pd.read_csv("Credit.csv") 
dt = dataset.iloc[:,[1,4,7]].values

#from sklearn.preprocessing import StandartScaler
from sklearn.preprocessing import MinMaxScaler

sc = StandartScaler()
x = sc.fit_transform(dt)

sc = MinMaxScaler()
y = sc.fit_transform(dt)
