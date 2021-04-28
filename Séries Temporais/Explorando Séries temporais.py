import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

base = pd.read_csv("AirPassengers.csv")

print(base.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv("AirPassengers.csv", parse_dates = ['Month'],
                   index_col = 'Month', date_parser = dateparse)

base.index

ts = base["#Passengers"]

ts[1]
ts ["1949 - 2"]
ts[datetime(1949,2,1)]

ts ["1950-01-01":"1950-07-31"]

ts [:"1950-07-31"]

ts["1950"]

ts.index.max()

ts.index.min()

plt.plot(ts)

ts_ano = ts.resample("A").sum()

plt.plot(ts_ano)

ts_mes = ts.groupby([lambda x: x.month]).sum()


plt.plot(ts_mes)
