import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

base = pd.read_csv("Eleicao.csv",sep = ";")

plt.scatter(base.DESPESAS, base.SITUACAO)

base.describe()

np.corrcoef(base.DESPESAS, base.SITUACAO)

x = base.iloc[:,2].values

x = x[:,np.newaxis]
y = base.iloc[:,1].values

modelo = LogisticRegression()
modelo.fit(x,y)

modelo.coef_
modelo.intercept_

x_teste = np.linspace(10,3000,100)

def model(x):
    return 1/(1+np.exp(-x))
r = model(x_teste*modelo.coef_ + modelo.intercept_).ravel()

base_previsões = pd.read_csv("NovosCandidatos.csv", sep = ";")
despesas = base_previsões.iloc[:,1].values
despesas = despesas.reshape(-1,1)
previsões_teste = modelo.predict(despesas)
