#!/usr/bin/python3
"""
script that lists all State objects from the database 'hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalehcmy.orm import sessionmaker

if __name___ == "__main__":
    """
    Addess to database and retrieve states from database
    """
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    for inst in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(inst.id, inst.name))
