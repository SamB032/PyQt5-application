from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import exists
import os.path

engine = create_engine("sqlite:///database.db")
session = sessionmaker(bind = engine)()

meta = MetaData()
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
        
if os.path.exists("database.db") == False:
    Base.metadata.tables["user"].create(bind = engine)
    Base.metadata.tables["note"].create(bind = engine)
    

#==================================Classes to interact with models====================================
class UserTable():
    def insert(self, name, username, password):
        user = User(name, username.lower(), generate_password_hash(password, method='sha256'))
        session.add(user)
        session.commit()
    
    def user_name_exsist(username):
        return session.query(exists().where(User.username == username.lower())).scalar()
        
    def check_credentials(username = "", password = ""):
        row = session.query(User).filter(User.username == username).first()
        
        try: 
            if check_password_hash(row.password, password) == True:
                return [True, row.user_id]
            else:
                return [False]
        except AttributeError:
            return [False]
        
class NoteTable():
    def insert(self, data, user_id):
        note = Note(data, user_id)
        session.add(note)
        session.commit()
    
    def return_user_notes(self, user_id):
        return session.query(Note).filter(Note.user_id == user_id)
    
    def delte_note(self, note_id):
        session.query(Note).filter(Note.note_id == note_id).delete()
        session.commit()