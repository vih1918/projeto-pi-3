from database import Base
from sqlalchemy import Column, Integer, String

class Animal(Base):
    __tablename__ = 'animais'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especie = Column(String)
