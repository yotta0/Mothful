from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class User(Base):
    __tablename__ =  'users'

    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    name = Column(String(60), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


    def __repr__(self):
        return f'username {self.username}'
