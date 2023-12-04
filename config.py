import os
from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent


class AppSettings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str
    debug: bool
    allowed_host: str
    secret_key: str
    redis_host: str
    redis_port: int
    access_key: str

    class Config:
        env_file = os.path.join(BASE_DIR, ".env.dev")


app_settings = AppSettings()
