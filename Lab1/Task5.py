import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")
model = GaussianNB()
X_train = pd.read_csv('./iris.csv')
le = LabelEncoder()
X_train["class"] = le.fit_transform(X_train["class"])
X_train = X_train.select_dtypes(include=[np.number]).interpolate().dropna()
numeric_features = X_train.select_dtypes(include=[np.number])

corr = numeric_features.corr()
print(corr)
X_train = X_train.drop(['sepal width'], axis=1)
train_df, test_df = train_test_split(X_train, test_size=0.4, random_state=0)
X_train = train_df.drop("class", axis=1)
Y_train = train_df["class"]
X_test = test_df.drop("class", axis=1)
Y_test = test_df["class"]

##Naive Bayes
model.fit(X_train, Y_train)
predicted= model.predict(X_test)
acc_nb = round(model.score(X_test, Y_test) * 100, 2)
print("Naive Bayes accuracy is:", acc_nb)

##SVM
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_test, Y_test) * 100, 2)
print("SVM accuracy is:", acc_svc)

##KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_test, Y_test) * 100, 2)
print("KNN accuracy is:",acc_knn)

