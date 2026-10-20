# Cross Validation Classification Accuracy
from pandas import read_csv
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import KFold, train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
seed = 7
num_folds = 10
kfold = KFold(n_splits=num_folds, shuffle=True, random_state=seed)

print("Accuracy")
model = LogisticRegression(max_iter=1000)
scoring = 'accuracy'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("Accuracy: ", results.mean(), results.std())

# Cross Validation Classification LogLoss]
print("Training loss")
model = LogisticRegression(max_iter=1000)
scoring = 'neg_log_loss'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("Logloss: ", results.mean(), results.std())


# Cross Validation Classification ROC AUC
print("ROC AUC")
model = LogisticRegression(max_iter=1000)
scoring = 'roc_auc'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print("AUC: ", results.mean(), results.std())

# Cross Validation Classification Confusion Matrix
test_size = 0.33
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
predicted = model.predict(X_test)
matrix = confusion_matrix(Y_test, predicted)
print(matrix)

# Cross Validation Classification Report
test_size = 0.33
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
predicted = model.predict(X_test)
report = classification_report(Y_test, predicted)
print(report)