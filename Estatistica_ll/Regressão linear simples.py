import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

base = pd.read_csv("cars.csv")
base = base.drop(['Unnamed: 0'],axis = 1)

x = base.iloc[:,1].values
x = x.reshape(-1,1)
y = base.iloc[:,0].values

correlacao = np.corrcoef(x,y)

modelo = LinearRegression()
modelo.fit(x,y)

modelo.intercept_
modelo.coef_

plt.scatter(x,y)

#distencia de 22 pés
modelo.intercept_+22*modelo.coef_

modelo.predict(22)

modelo._residues


