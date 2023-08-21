#!/usr/bin/python3
"""State model interface for sqlalchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class that represent the states sql table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
