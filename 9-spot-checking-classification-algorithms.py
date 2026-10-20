# Logistic Regression Classification
from pandas import read_csv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)

#logistic regression model
print("Logistic regression")
model = LogisticRegression()
model = LogisticRegression(max_iter=1000)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

# Linear Discriminant Analysis (LDA) Classification
print("Linear discriminant analysis (LDA) classification")
model = LinearDiscriminantAnalysis()
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

#Non-linear ML algorithms
print("Non-linear ML algorithms")
# KNN Classification
print("k-Nearest Neighbour ML algorithms")
model = KNeighborsClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
print()

# Classification and regression trees (CART) Classification
print("Classification and regression trees (CART) ML algorithms")
model = DecisionTreeClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
print()


# Gaussian Naive Bayes Classification
print("Gaussian Naive Bayes ML algorithms")
model = GaussianNB()
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())
print()

# support vector machines (SVM) Classification
print("Support Vector Machines (SVM) ML algorithms")
model = SVC()
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())