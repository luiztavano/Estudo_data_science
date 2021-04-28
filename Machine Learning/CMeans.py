from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import skfuzzy

iris = datasets.load_iris()

r = skfuzzy.cmeans(data = iris.data.T, c = 3, m = 2, error = 0.005, maxiter = 100, init = None)

previsoes_porcentagem = r[1]

previsoes = previsoes_porcentagem.argmax(axis = 0)
resultados = confusion_matrix(iris.target, previsoes)