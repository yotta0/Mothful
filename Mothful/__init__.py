from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object('config')

db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=db)
session = Session()

from . import views
