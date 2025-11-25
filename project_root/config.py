import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "your_secret_key_here"

    # Database lives INSIDE project_root/
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Uploads folder also inside project_root/instance/uploads
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "instance", "uploads")
