#!/usr/bin/python3
"""City model interface for sqlalchemy"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base, State


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey(State.id))
