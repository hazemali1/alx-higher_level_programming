#!/usr/bin/python3
"""
class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base




class City(Base):
    """id and name"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
