import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19,6], [42,32]])

chi2_contingency(novela)
