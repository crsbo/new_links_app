import os

class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # هذا هو الرابط الذي ستضعه من Railway.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
