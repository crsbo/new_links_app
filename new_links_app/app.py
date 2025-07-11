import os
from flask import Flask

app = Flask(__name__)

# استخدم مكتبة os للوصول للمتغيرات البيئية
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

@app.route('/')
def home():
    return "Hello, Railway!"
