
import os

class Config:
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
