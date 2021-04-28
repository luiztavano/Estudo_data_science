from scipy.stats import poisson

#Média de acidentes de carro é igual a 2 por dia
#Qual a probabilidade de ocorrerem 3 por dia?
poisson.pmf(3,2)

#Qual a probabilidade de ocorrerem 3 ou menos por dia?
poisson.cdf(3,2)

#Qual a probabilidade de ocorrerem 3 ou mais por dia?
poisson.sf(3,2)



