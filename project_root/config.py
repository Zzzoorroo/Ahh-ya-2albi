import os

class Config:
    SECRET_KEY = 'ba9i-ma3ndix'
    UPLOAD_FOLDER = os.path.join("instance","uploads")
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024 #20MB UPLOAD LIMIT


    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False