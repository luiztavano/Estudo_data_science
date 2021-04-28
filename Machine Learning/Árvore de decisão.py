import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier

credito = pd.read_csv("Credit.csv")
previsores = credito.iloc[:,0:20].values
classes = credito.iloc[:,20].values

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])

X_treinamento, X_teste, Y_treinamento, Y_teste = train_test_split(previsores,
                                                                  classes,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, Y_treinamento)

previsoes = arvore.predict(X_teste)
confusao = confusion_matrix(Y_teste, previsoes)
taxa_acerto = accuracy_score(Y_teste,previsoes)
taxa_erro = 1 - taxa_acerto
