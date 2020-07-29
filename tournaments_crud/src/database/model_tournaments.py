from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint


class ModelTournaments(Base):
    """Tournament Model """
    __tablename__ = 'tournaments'

    id = Column('id', Integer, primary_key=True, doc='PK of Tournament.')
    name = Column('name', String, doc='Name of tournament', nullable=False,
            unique=True)
    max_participants = Column('max_participants', Integer, default=16)
    min_participants = Column('min_participants', Integer, default=2)
    created = Column('created', String, doc="Creation date of Tournament.")
    edited = Column('edited', String, doc="Edited date of Tournament.")
    participants = Column('participants', String, doc="String of global IDs")

    UniqueConstraint(name)
