import os
from dotenv import load_dotenv

load_dotenv()

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-in-prod")
    default_db = "sqlite:///" + os.path.join(BASEDIR, "instance", "database.db")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", default_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_MOCK_URL = os.getenv("API_MOCK_URL", "http://localhost:5000/api/agendamentos")
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
