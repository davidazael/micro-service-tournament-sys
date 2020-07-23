from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelUsers(Base):
    """ Users Model 
    * Users can Create a Tournament.
    * Users can participate in zero, one, or more tournaments.
    All of the variable names must match in Schema, lambda functions will use
    the variable names."""

    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, doc='PK Id of User.')
    name = Column('name', String, doc="Name of User.")
    first_name = Column('first_name', String,nullable=False, doc="First Name of User.")
    middle_name = Column('middle_name', String, doc="Middle Name of User.")
    last_name = Column('last_name', String, nullable=False, doc="Last Name of User.")
    steam_Id = Column('steamId', Integer, doc="Steam ID of User.")
    created = Column('created', String, doc="Creation time of User.")
    edited = Column('edited', String, doc="Edited time of User.")
    owner_tournament = Column('owner_tournament', ARRAY(String), doc="Stores of global IDs this user has created.")

