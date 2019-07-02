import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("breas_cancer.csv").values
print(dataset)
x = dataset[:,1:2]
x = le.fit_transform(x)
#dataset = dataset.drop(['diagnosis'], axis=1)
# print(dataset)
import numpy as np
print(dataset[:,2:32])
print(x)
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,2:32], x,
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(40, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(20, activation='relu'))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))
