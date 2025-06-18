import joblib
import numpy as np
from loguru import logger
from sklearn.base import BaseEstimator
from typing import Union

class ModelHandler:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model: Union[BaseEstimator, None] = None

    def load_model(self):
        try:
            self.model = joblib.load(self.model_path)
            logger.info(f"Model loaded from {self.model_path}")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise

    def predict(self, features: np.ndarray) -> int:
        if self.model is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        prediction = self.model.predict(features.reshape(1, -1))[0]
        logger.debug(f"Prediction: {prediction}")
        return prediction
