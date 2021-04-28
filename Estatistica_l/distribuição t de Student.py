from scipy.stats import t

#Média de salário dos cientistas de dados é de R$75,00 a hora
# Amostra com 9 funcionários e desvio padrão de 10

# Qual a probabilidade de selecionar um cientista de dados e o salário ser menor de R$80,00 a hora

t.cdf(1.5,8)

# Qual a probabilidade de selecionar um cientista de dados e o salário ser maior de R$80,00 a hora
t.sf(1.5,8)