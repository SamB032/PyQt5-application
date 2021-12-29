from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import exists
import os.path
import models

engine = create_engine("sqlite:///database.db")
session = sessionmaker(bind = engine)()

meta = MetaData()
    
if os.path.exists("database.db") == False:
    Base.metadata.tables["user"].create(bind = engine)
    Base.metadata.tables["note"].create(bind = engine)

#==================================Classes to interact with models====================================
class UserTable():
    def insert(self, name, username, password):
        user = models.User(name, username.lower(), generate_password_hash(password, method='sha256'))
        session.add(user)
        session.commit()
    
    def user_name_exsist(username):
        return session.query(exists().where(models.User.username == username.lower())).scalar()
        
    def check_credentials(username = "", password = ""):
        row = session.query(models.User).filter(models.User.username == username).first()
        
        try: 
            if check_password_hash(row.password, password) == True:
                return [True, row.user_id]
            else:
                return [False]
        except AttributeError:
            return [False]
        
class NoteTable():
    def insert(self, data, user_id):
        note = models.Note(data, user_id)
        session.add(note)
        session.commit()
    
    def return_user_notes(self, user_id):
        return session.query(models.Note).filter(models.Note.user_id == user_id)
    
    def delte_note(self, note_id):
        session.query(models.Note).filter(models.Note.note_id == note_id).delete()
        session.commit()