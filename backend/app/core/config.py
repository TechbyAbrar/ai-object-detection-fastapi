from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_path: str = "models/yolov8n.pt"

    upload_dir: str = "app/storage/uploads"
    output_dir: str = "app/storage/outputs"

    api_prefix: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()