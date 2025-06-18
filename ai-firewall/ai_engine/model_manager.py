import joblib
import onnxruntime as ort
import numpy as np
from loguru import logger
from pathlib import Path

class ModelManager:
    def __init__(self, model_dir: str):
        self.model_dir = Path(model_dir)
        self.models = {}

    def load_sklearn_model(self, name: str):
        path = self.model_dir / f"{name}.joblib"
        logger.info(f"Loading sklearn model: {path}")
        self.models[name] = joblib.load(path)

    def load_onnx_model(self, name: str):
        path = self.model_dir / f"{name}.onnx"
        logger.info(f"Loading ONNX model: {path}")
        self.models[name] = ort.InferenceSession(str(path))

    def predict(self, name: str, data: np.ndarray) -> np.ndarray:
        model = self.models.get(name)
        if isinstance(model, ort.InferenceSession):
            inputs = {model.get_inputs()[0].name: data.astype(np.float32)}
            return model.run(None, inputs)[0]
        elif hasattr(model, 'predict'):
            return model.predict(data)
        else:
            raise ValueError(f"No valid model found with name: {name}")
