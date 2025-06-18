import joblib
import os
from ai_firewall.config.config import settings

def load_model(model_name: str):
    model_path = os.path.join(settings.MODEL_DIR, f"{model_name}.joblib")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model {model_path} not found")
    return joblib.load(model_path)
