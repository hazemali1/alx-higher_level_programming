#!/usr/bin/python3
"""
class
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    s = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(s)

    Session = sessionmaker(bind=s)
    d = Session()

    result = d.query(State).order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for c in state.cities:
            print("\t{}: {}".format(c.id, c.name))
