from sqlalchemy import Column, Integer, String
from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)