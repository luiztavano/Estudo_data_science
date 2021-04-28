from scipy.stats import binom

#Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?

prob = binom.pmf(3,5,0.5)

# passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde em:
# nenhuma, 1, 2, 3 ou 4 vezes seguidas?

binom.pmf(4,4,0.25)

#probabilidade acumulativa
binom.cdf(4,4,0.25)
