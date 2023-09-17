#!/usr/bin/python3
"""
class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
	"""id and name"""
	__tablename__ ='states'
	id = Column(Integer, autoincrement=True, primary_key=True)
	name = Column(String(128), nullable=False)
	