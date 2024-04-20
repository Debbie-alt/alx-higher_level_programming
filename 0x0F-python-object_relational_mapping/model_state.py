#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql://username:password@localhost:3306/database_name')

    # WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)

