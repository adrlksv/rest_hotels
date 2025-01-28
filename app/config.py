from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    TEST_DB_HOST: str
    TEST_DB_PORT: str
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
    
    SMTP_PORT : int
    SMTP_HOST : str
    SMTP_USER : str
    SMTP_PASS : str

    REDIS_HOST: str
    REDIS_PORT: int

    SECRET_KEY: str
    ENCRYPT: str

    class Config:
        env_file = ".env"


settings = Settings()

# load_dotenv()


# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_NAME = os.getenv("DB_NAME")
# SECRET_KEY = os.getenv("SECRET_KEY")
# ENCRYPT = os.getenv("ENCRYPT")

# TEST_DB_HOST = os.getenv("TEST_DB_HOST")
# TEST_DB_PORT = os.getenv("TEST_DB_PORT")
# TEST_DB_USER = os.getenv("TEST_DB_USER")
# TEST_DB_PASS = os.getenv("TEST_DB_PASS")
# TEST_DB_NAME = os.getenv("TEST_DB_NAME")

# REDIS_HOST = os.getenv("REDIS_HOST")
# REDIS_PORT = os.getenv("REDIS_PORT")

# SMTP_PORT = os.getenv("SMTP_PORT")
# SMTP_HOST = os.getenv("SMTP_HOST")
# SMTP_USER = os.getenv("SMTP_USER")
# SMTP_PASS = os.getenv("SMTP_PASS")

# MODE = os.getenv(Literal["DEV", "TEST", "Prod"])
