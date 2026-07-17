from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# ชี้ไปยังโฟลเดอร์ backend/ (.parent.parent จาก backend/core/config.py)
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    redis_host: str = "localhost"
    redis_port: int = 6379
    
    postgres_user: str = "labeluser"
    postgres_password: str = "labelpassword"
    postgres_db: str = "labelstudio_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    
    label_studio_url: str = "http://localhost:8080"
    label_studio_api_key: str = ""
    
    # กำหนดค่าสำหรับโหลดไฟล์ .env ด้วย Absolute Path
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
