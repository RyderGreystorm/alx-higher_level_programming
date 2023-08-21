#!/usr/bin/python3

"""List all City objects with their associated State names using SQLAlchemy"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def run():
    """Begin code execution"""

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id).all()

    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))


if __name__ == '__main__':
    run()
