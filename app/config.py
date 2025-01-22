from dotenv import load_dotenv

import os


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
ENCRYPT = os.getenv("ENCRYPT")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")