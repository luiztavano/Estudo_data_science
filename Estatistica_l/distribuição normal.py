from scipy.stats import norm

#conjunto com objetos de uma cesta, média de 8 e desvio padrão de 2
# Qual a probabilidade de tirar um objeto que o peso é menor que 6 quilos?

norm.cdf(6, 8,2)

# Qual a probabilidade de tirar um objeto que o peso é maior que 6 quilos?
#Existem duas maneiras de calcular isso.

norm.sf(6,8,2)

1 - norm.cdf(6, 8,2)

# Qual a probabilidade de tirar um objeto que o peso é menor que 6 quilos ou maior que 10?

norm.cdf(6,8,2) + norm.sf(10,8,2)

# Qual a probabilidade de tirar um objeto que o peso é maior que 8 quilos e menor que 10?

norm.cdf(10,8,2) - norm.cdf(8,8,2)