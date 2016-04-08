#get your data

import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target

#split your data 

ntest=10
np.random.seed(0)
indices = np.random.permutation(len(X))

iris_X_train = X[indices[:-ntest]]
iris_Y_train = Y[indices[:-ntest]]

iris_X_test = X[indices[-ntest:]]
iris_Y_test = Y[indices[-ntest:]]
'''
print(iris_X_train)
print(iris_Y_train)

print(iris_X_test)
print(iris_Y_test)
'''
#fit your model

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski')
knn.fit(iris_X_train, iris_Y_train)

#check your model

predicted_classes = knn.predict(iris_X_test)

print('kNN predicted classes: {}'.format(predicted_classes))
print('Real classes:          {}'.format(iris_Y_test))

#metrics

from sklearn import metrics
print(metrics.classification_report(iris_Y_test, predicted_classes))