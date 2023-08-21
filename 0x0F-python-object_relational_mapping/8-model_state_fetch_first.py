#!/usr/bin/python3
"""Execute some sql queries using sqlalchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


def run():
    """Begin code execution"""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # execute query
    query = session.query(State).order_by(State.id)
    state = query.first()
    if state is None:
        print('Nothing')
    else:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    run()
