# Linear Regression
from random import seed

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

seed = 7
num_folds = 10
kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)
scoring = 'neg_mean_squared_error'

print("Linear Regression")
model = LinearRegression()
lrResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring, error_score='raise')
print(lrResults.mean())

# Ridge Regression
print("Ridge Regression")
model = Ridge()
rrResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring, error_score='raise')
print(rrResults.mean())

# Lasso Regression
print("Lasso Regression")
model = Lasso()
lassoResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(lassoResults.mean())


# ElasticNet Regression
print("ElasticNet Regression")
model = ElasticNet()
erResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(erResults.mean())


# non-linear ML algorithms
# KNN Regression
print("KNN Regression")
model = KNeighborsRegressor()
kResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(kResults.mean())


# Decision Tree Regression
print("Decision Tree Regression")
model = DecisionTreeRegressor()
dResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(dResults.mean())

# SVM Regression
print("SVM Regression")
model = SVR()
svmResults = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(svmResults.mean())
