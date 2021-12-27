from sqlalchemy import (create_engine, MetaData)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import exists
import os.path

engine = create_engine("sqlite:///database.db")
session = sessionmaker(bind = engine)()

Base = declarative_base()
meta = MetaData()

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
        
if os.path.exists("database.db") == False:
    Base.metadata.tables["user"].create(bind = engine)


#==================================Classes to interact with db====================================
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
                return True
            else:
                return False
        except AttributeError:
            return False