import numpy as np
from loguru import logger
from ai_firewall.ai_engine.model_handler import ModelHandler

class ThreatDetector:
    def __init__(self, model_manager: ModelManager, model_name: str):
        self.model_manager = model_manager
        self.model_name = model_name

    def is_malicious(self, features: np.ndarray) -> bool:
        logger.debug(f"Running prediction on features: {features}")
        result = self.model_manager.predict(self.model_name, features)
        threat = result[0] if isinstance(result, (list, np.ndarray)) else result
        logger.info(f"Threat score: {threat}")
        return bool(threat > 0.5)

    def extract_features(self, packet_data: dict) -> np.ndarray:
        # Basic example - replace with domain-specific logic
        try:
            features = np.array([
                float(packet_data.get("packet_length", 0)),
                float(packet_data.get("ttl", 0)),
                float(packet_data.get("src_port", 0)),
                float(packet_data.get("dst_port", 0)),
            ])
            logger.debug(f"Extracted features: {features}")
            return features
        except Exception as e:
            logger.error(f"Feature extraction failed: {e}")
            raise

    def detect(self, packet_data: dict) -> dict:
        features = self.extract_features(packet_data)
        label = self.model_handler.predict(features)
        return {
            "threat_detected": bool(label),
            "confidence": 1.0,  # Add confidence score if your model supports it
            "features": features.tolist()
        }
