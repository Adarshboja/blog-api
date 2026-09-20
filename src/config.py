"""Application configuration."""

import os


APP_ENV = os.getenv("APP_ENV", "development")
APP_PORT = int(os.getenv("PORT", "8000"))
