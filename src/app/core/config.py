from functools import lru_cache
from typing import Literal

from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.local",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = "nm-portfolio-api"
    APP_ENV: Literal["local", "dev", "staging", "prod"] = "local"
    APP_DEBUG: bool = False
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    API_BASE_URL: str = "http://127.0.0.1:8000"

    CORS_ALLOW_ORIGINS: str = ""

    DATABASE_URL: str | None = None
    REDIS_URL: str | None = None

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    SENTRY_DSN: str | None = None
    SMTP_HOST: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USERNAME: str | None = None
    SMTP_PASSWORD: str | None = None

    @field_validator(
        "DATABASE_URL",
        "REDIS_URL",
        "SENTRY_DSN",
        "SMTP_HOST",
        "SMTP_USERNAME",
        "SMTP_PASSWORD",
        mode="before",
    )
    @classmethod
    def empty_string_to_none_for_optional_strings(cls, value: object) -> object:
        if isinstance(value, str) and value.strip() == "":
            return None
        return value

    @field_validator("SMTP_PORT", mode="before")
    @classmethod
    def empty_string_to_none_for_optional_int(cls, value: object) -> object:
        if value is None:
            return None
        if isinstance(value, str) and value.strip() == "":
            return None
        return value

    @field_validator("SECRET_KEY")
    @classmethod
    def validate_secret_key(cls, value: str) -> str:
        if len(value.strip()) < 24:
            raise ValueError("SECRET_KEY must be at least 24 characters long.")
        return value

    @model_validator(mode="after")
    def validate_production_requirements(self) -> "Settings":
        if self.APP_ENV == "prod" and not self.DATABASE_URL:
            raise ValueError("DATABASE_URL is required when APP_ENV=prod.")
        return self

    @property
    def cors_allow_origins(self) -> list[str]:
        if not self.CORS_ALLOW_ORIGINS.strip():
            return []
        return [item.strip() for item in self.CORS_ALLOW_ORIGINS.split(",") if item.strip()]

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "prod"

    def safe_summary(self) -> dict[str, object]:
        return {
            "app_name": self.APP_NAME,
            "app_env": self.APP_ENV,
            "app_debug": self.APP_DEBUG,
            "log_level": self.LOG_LEVEL,
            "api_base_url": self.API_BASE_URL,
            "cors_allow_origins": self.cors_allow_origins,
            "database_configured": self.DATABASE_URL is not None,
            "redis_configured": self.REDIS_URL is not None,
            "sentry_configured": self.SENTRY_DSN is not None,
            "smtp_configured": all(
                value is not None
                for value in (
                    self.SMTP_HOST,
                    self.SMTP_PORT,
                    self.SMTP_USERNAME,
                    self.SMTP_PASSWORD,
                )
            ),
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()
