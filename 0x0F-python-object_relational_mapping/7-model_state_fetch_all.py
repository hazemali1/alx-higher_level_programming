#!/usr/bin/python3
"""
class
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    s = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base.metadata.create_all(s)

Session = sessionmaker(bind=engine)
d = Session()

result = d.query(State).order_by(State.id).all()

for state in result:
    print("{}: {}".format(state.id, state.name))
