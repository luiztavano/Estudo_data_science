import pandas as pd 'importar as bibliotecas'
import numpy as np

base =pd.read_csv('iris.csv') 'definit um objeto que receberá a base de dados'

base 'exibir a base de dados'

base.shape 'exibir as informções da base de dados'

amostra = np.random.choice(a = [0,1], size = 150, replace = True, p =[0.5, 0.5])
'gerar amostra'

