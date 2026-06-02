import os

class Settings:
    # Деплой кезінде бұл айнымалылар серверден алынады
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/online_shop")
    SECRET_KEY = os.getenv("SECRET_KEY", "SUPER_SECRET_KEY_123")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
