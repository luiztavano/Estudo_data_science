import pandas as pd
import scipy as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

tratamento = pd.read_csv("anova.csv", sep = ";")

tratamento.boxplot(by="Remedio")

modelo1 = ols("Horas ~ Remedio", data = tratamento).fit ()
resultados1 = sm.stats.anova_lm(modelo1)

modelo2 = ols("Horas ~ Remedio * Sexo", data = tratamento).fit ()
resultados2 = sm.stats.anova_lm(modelo2)

mc = MultiComparison(tratamento["Horas"], tratamento["Remedio"])
Resultado_teste = mc.tukeyhsd()
print(Resultado_teste)



