from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String)
    role = Column(String, default="user")
    
