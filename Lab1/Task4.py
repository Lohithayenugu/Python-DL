import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = load_diabetes(return_X_y=False)

data = pd.DataFrame(data= np.c_[train['data'], train['target']],columns= train['feature_names'] + ['target'])

data = data.select_dtypes(include=[np.number]).interpolate().dropna()
numeric_features = data.select_dtypes(include=[np.number])

corr = numeric_features.corr()
print(corr)
data = data.drop(['s3'], axis=1)
X = data.drop(['target'], axis=1)
Y = data['target']
X_train, X_test,y_train, y_test = train_test_split(X, Y, random_state=42, test_size=.33)

from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

##visualize

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75, color='b')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Linear Regression Model')
plt.show()
