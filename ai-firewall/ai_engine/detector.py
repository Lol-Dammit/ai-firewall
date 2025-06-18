from pyod.models.knn import KNN
import numpy as np

class TrafficAnomalyDetector:
    def __init__(self):
        self.model = KNN()
        self._is_trained = False

    def train(self, X: np.ndarray):
        self.model.fit(X)
        self._is_trained = True

    def detect(self, X: list[list[float]]):
        if not self._is_trained:
            self.train(np.array(X))  # Quick bootstrapping
        return self.model.predict(np.array(X))