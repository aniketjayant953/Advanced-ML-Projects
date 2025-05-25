import numpy
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from KNeighboursClassifier import Mera_Knn

df = pd.read_csv('Social_Network_Ads.csv')

df = df.iloc[:, 1:]
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

X = df.iloc[:, 0:3].values
y = df.iloc[:, -1].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

apnaKnn = Mera_Knn(k=5)

apnaKnn.fit(X_train, y_train)
y_pred1 = apnaKnn.predict(X_test)

accuracy1 = accuracy_score(y_test, y_pred1)
print(accuracy1)
