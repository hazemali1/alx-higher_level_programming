#!/usr/bin/python3
"""
class
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City


if __name__ == "__main__":
    s = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(s)

    Session = sessionmaker(bind=s)
    d = Session()

    result = d.query(State, City).join(City).order_by(City.id)

    for state, city in result:
        print("{}: ({}) {}".format(state.id, city.id, city.name))
