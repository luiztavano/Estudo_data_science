import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("iris.csv")

plt.boxplot(iris.iloc[:,1],showfliers = True)

outliers = iris[(iris["sepal width"]>4.0) | (iris["sepal width"]<2.1)]


