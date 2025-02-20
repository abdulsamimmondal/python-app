import os

class Config:
    FLASK_APP = 'app.py'
    FLASK_ENV = 'development'
    SECRET_KEY = os.urandom(24)
    API_BASE_URL = "https://jsonplaceholder.typicode.com"
