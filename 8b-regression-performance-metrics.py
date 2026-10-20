# Cross Validation Regression mean absolute error (MAE)
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]

seed = 7
num_folds = 10
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

print("Linear Regression => Mean Absolute Error")
model = LinearRegression()
model = LinearRegression()
scoring = 'neg_mean_absolute_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring, error_score='raise')
print("MAE: ", results.mean(), results.std())

# Cross Validation Regression mean squared error (MSE)
print("Linear Regression => Mean Square Error")
model = LinearRegression()
model = LinearRegression()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring, error_score='raise')
print("MSE: ", results.mean(), results.std())


# Cross Validation Regression R^2
print("Linear Regression => R Squared Error")
model = LinearRegression()
scoring = 'neg_mean_absolute_error'
model = LinearRegression()
scoring = 'r2'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring, error_score='raise')
print("R^2: ", results.mean(), results.std())


