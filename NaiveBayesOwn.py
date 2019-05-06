import numpy as np

class NaiveBayes:
    def __init__(self):
        self.features = None
        self.__classes = None
        self.__stats = {}
    def fit(self, X, y):
        self.__classes = np.unique(y)
        k = len(self.__classes)
        for j in range(0, X.shape[1]):
            if len(np.unique(X[:, j])) > 2:
                if self.features != None:
                    self.features = self.discretize(X[:, j])
                else:
                    self.features = np.hstack(( self.features, self.discretize(X[:, j]) ))
            else:
                value_of_feature = X[0, j]
                if self.features != None:
                    self.features = X[:, j:j+1] == value_of_feature
                else:
                    self.features = np.hstack((self.features, X[:, j:j+1] == value_of_feature))
        for classk in self.__classes:
            self.__stats[classk] = np.sum(self.features[y == classk, :], axis = 0) 
    def discretize(self, feature):
        NewFeatureSet = np.array([])
        q = [1, 25, 50, 75]
        percentiles = np.percentile(feature, q)
        for percentile in percentiles:
            feature_new = feature < percentile
            feature_new = feature.reshape(feature_new.size, 1)
            if np.array_equal(NewFeatureSet, np.array([])):
                NewFeatureSet = feature_new
            else:
                NewFeatureSet = np.hstack((NewFeatureSet, feature_new))
        return NewFeatureSet