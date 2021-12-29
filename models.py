from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key = True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

class Note(Base):
    __tablename__ = "note"
    note_id = Column(Integer, primary_key = True)
    data = Column(String(10000))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    notes = relationship('User')
    
    def __init__(self, data, user_id):
        self.data = data
        self.user_id = user_id