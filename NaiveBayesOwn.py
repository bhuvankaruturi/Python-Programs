<<<<<<< HEAD
import numpy as np

class NaiveBayes:
    def __init__(self):
        self.features = np.array([])
        self.classes = np.array([])
        self.total = np.array([])
        self.stats = np.array([])

    def fit(self, X, y):
        self.classes = np.unique(y)
        self.features = self.generateFeatures(X)
        self.generateStats(y)

    def generateFeatures(self, X):
        all_features = np.array([])
        for j in range(0, X.shape[1]):
            if np.issubdtype(X.dtype, int) or np.issubdtype(X.dtype, float):
                if np.array_equal(all_features, np.array([])):
                    all_features = self.discretize(X[:, j])
                else:
                    all_features = np.hstack((all_features, self.discretize(X[:, j]) ))
            else:
                value_of_feature = X[0, j]
                if np.array_equal(all_features, np.array([])):
                    all_features = X[:, j:j+1] == value_of_feature
                else:
                    all_features = np.hstack((all_features, X[:, j:j+1] == value_of_feature))
        return all_features

    def generateStats(self, y):
        for classk in self.classes:
            if np.array_equal(self.stats, np.array([])):
                self.stats = np.sum(self.features[y == classk, :], axis = 0)
            else:
                self.stats = np.vstack((self.stats, np.sum(self.features[y == classk, :], axis = 0)))
            self.total = np.append(self.total, np.sum(y==classk, axis=0))

    def predict(self, X):
        X_new = self.generateFeatures(X)
        print(X_new)
        max_prob = 0
        targetclass = None
        for k in range(0, self.stats.shape[0]):
            print("total in class", k, "is:", self.total[k])
            classi_prob = 1
            for i in range(0, self.stats[k].size):
                if X_new[0, i]:
                    classi_prob = classi_prob * (self.stats[k, i]/self.total[k])
                else:
                    classi_prob = classi_prob * (1 - (self.stats[k, i]/self.total[k]))
            classi_prob = classi_prob * (self.total[k] * np.sum(self.total))
            if classi_prob > max_prob:
                max_prob = classi_prob
                targetclass = k
            print('prob of class:', k, '-', classi_prob)
        return targetclass

    def discretize(self, feature):
        NewFeatureSet = np.array([])
        q = [20, 40, 60, 80, 100]
        percentiles = np.percentile(feature, q)
        prev_percentile = None
        for percentile in percentiles:
            if prev_percentile == None:
                feature_new = feature <= percentile
            else:
                feature_new = np.all([feature > prev_percentile,feature <= percentile], axis=0)
            feature_new = feature_new.reshape(feature_new.size, 1)
            if np.array_equal(NewFeatureSet, np.array([])):
                NewFeatureSet = feature_new
            else:
                NewFeatureSet = np.hstack((NewFeatureSet, feature_new))
            prev_percentile = percentile
        return NewFeatureSet

from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target

nbc = NaiveBayes()
nbc.fit(X, y)
n = 111
print(nbc.stats)
print(nbc.total)
print('_____________')
print(X[n])
print(y[n])
print('_____________')
print(nbc.predict(X[n:n+1, :]))
=======
import numpy as np

class NaiveBayes:
    def __init__(self):
        self.features = np.array([])
        self.classes = np.array([])
        self.total = np.array([])
        self.stats = np.array([])

    def fit(self, X, y):
        self.classes = np.unique(y)
        self.features = self.generateFeatures(X)
        self.generateStats(y)

    def generateFeatures(self, X):
        all_features = np.array([])
        for j in range(0, X.shape[1]):
            if np.issubdtype(X.dtype, int) or np.issubdtype(X.dtype, float):
                if np.array_equal(all_features, np.array([])):
                    all_features = self.discretize(X[:, j])
                else:
                    all_features = np.hstack((all_features, self.discretize(X[:, j]) ))
            else:
                value_of_feature = X[0, j]
                if np.array_equal(all_features, np.array([])):
                    all_features = X[:, j:j+1] == value_of_feature
                else:
                    all_features = np.hstack((all_features, X[:, j:j+1] == value_of_feature))
        return all_features

    def generateStats(self, y):
        for classk in self.classes:
            if np.array_equal(self.stats, np.array([])):
                self.stats = np.sum(self.features[y == classk, :], axis = 0)
            else:
                self.stats = np.vstack((self.stats, np.sum(self.features[y == classk, :], axis = 0)))
            self.total = np.append(self.total, np.sum(y==classk, axis=0))

    def predict(self, X):
        X_new = self.generateFeatures(X)
        print(X_new)
        max_prob = 0
        targetclass = None
        for k in range(0, self.stats.shape[0]):
            print("total in class", k, "is:", self.total[k])
            classi_prob = 1
            for i in range(0, self.stats[k].size):
                if X_new[0, i]:
                    classi_prob = classi_prob * (self.stats[k, i]/self.total[k])
                else:
                    classi_prob = classi_prob * (1 - (self.stats[k, i]/self.total[k]))
            classi_prob = classi_prob * (self.total[k] * np.sum(self.total))
            if classi_prob > max_prob:
                max_prob = classi_prob
                targetclass = k
            print('prob of class:', k, '-', classi_prob)
        return targetclass

    def discretize(self, feature):
        NewFeatureSet = np.array([])
        q = [20, 40, 60, 80, 100]
        percentiles = np.percentile(feature, q)
        prev_percentile = None
        for percentile in percentiles:
            if prev_percentile == None:
                feature_new = feature <= percentile
            else:
                feature_new = np.all([feature > prev_percentile,feature <= percentile], axis=0)
            feature_new = feature_new.reshape(feature_new.size, 1)
            if np.array_equal(NewFeatureSet, np.array([])):
                NewFeatureSet = feature_new
            else:
                NewFeatureSet = np.hstack((NewFeatureSet, feature_new))
            prev_percentile = percentile
        return NewFeatureSet

from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target

nbc = NaiveBayes()
nbc.fit(X, y)
n = 111
print(nbc.stats)
print(nbc.total)
print('_____________')
print(X[n])
print(y[n])
print('_____________')
print(nbc.predict(X[n:n+1, :]))
>>>>>>> 77b77e16ff4a7e57123b0d70a1b48ccc29c79638
