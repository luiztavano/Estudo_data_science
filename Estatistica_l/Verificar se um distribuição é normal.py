#Algoritmo para verificar se um distribuição é normal
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

dados = norm.rvs(size = 100) 

stats.probplot(dados,plot = plt)

#teste de shapiro

stats.shapiro(dados)
