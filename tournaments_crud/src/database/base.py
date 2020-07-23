from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

# Creating DB Engine
db_name = 'database_tournament.db'
db_path = os.path.join(os.path.dirname(__file__), db_name)
db_uri = 'sqlite:///{}'.format(db_path)
engine = create_engine(db_uri, convert_unicode=True)

# DeclarativeBase model to create database entities.
Base = declarative_base()
Base.metadata.bind = engine # Bind engine to metadata of base class.

db_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
Base.query = db_session.query_property() # Used by graphql to execute queries
