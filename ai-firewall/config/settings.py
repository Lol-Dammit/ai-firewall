from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Adaptive AI Firewall"
    environment: str = "development"
    model_path: str = "./models"
    log_level: str = "info"
    kafka_broker: str = "localhost:9092"
    s3_bucket_name: str = "ai-firewall-logs"
    database_url: str = "postgresql://user:pass@localhost/firewall

    class Config:
        env_file = ".env"

settings = Settings()
