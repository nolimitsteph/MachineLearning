# Evaluate using a train and a test set
from pandas import read_csv
from sklearn.model_selection import train_test_split, KFold, cross_val_score, LeaveOneOut, ShuffleSplit
from sklearn.linear_model import LogisticRegression
filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
print(array)

X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
num_folds = 10

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression(max_iter=1000) # here we are stating the number of iterations as 1000
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)
print("Accuracy: ", result*100.0)

#k-fold validation
print("k-fold validation")
loocv = LeaveOneOut()
kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)
model = LogisticRegression(max_iter=1000)
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: ", results.mean()*100.0, results.std()*100.0)

# Evaluate using Leave One Out Cross Validation
print("Leave one out cross validation")
loocv = LeaveOneOut()
model = LogisticRegression(max_iter=1000)
results = cross_val_score(model, X, Y, cv=loocv)
print("Accuracy: ", results.mean()*100.0, results.std()*100.0)

# Evaluate using Shuffle Split Cross Validation
print("Shuffle Split Cross Validation")
n_splits = 10
test_size = 0.33
kfold = ShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=seed)
model = LogisticRegression(max_iter=1000)
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy: ", results.mean()*100.0, results.std()*100.0)

