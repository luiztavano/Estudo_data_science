import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA

base = pd.read_csv("AirPassengers.csv")
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv("AirPassengers.csv", parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)
ts = base["#Passengers"]

plt.plot(ts)

#p, q, d

modelo = ARIMA(ts, order =(2,1,2))
modelo_treinado = modelo.fit()
modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps = 12) [0]

eixo = ts.plot()
modelo_treinado.plot_predict("1960 - 01 - 01", "1962 - 01 - 01",
                             ax = eixo, plot_insample = True)