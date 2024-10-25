from dotenv import load_dotenv
from flask import Flask
import logging
import os

from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URI'] = os.getenv('DATABASE_URI')

db = SQLAlchemy(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
