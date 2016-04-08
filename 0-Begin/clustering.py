#get your data

from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target
print("Xs: {}".format(X))

#fit model to data
from sklearn import cluster

k_means = cluster.KMeans(3)
k_means.fit(iris.data)

#check your model
print("Generated labels: \n{}".format(k_means.labels_))
print("Real labels: \n{}".format(Y))