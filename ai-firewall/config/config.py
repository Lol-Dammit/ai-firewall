from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MODEL_DIR: str = "ai_firewall/ai_engine/models/"
    KAFKA_BROKER: str = "localhost:9092"

    class Config:
        env_file = ".env"

settings = Settings()
