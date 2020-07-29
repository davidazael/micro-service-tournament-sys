import graphene
from graphene.types.resolver import dict_resolver
from graphene import Int, ID, Boolean, String, InputObjectType, ObjectType
from . import utils
from . import client

''' 
- Because this is a micro-service we need to tell this query what to expect from
the models itself. 
'''

class User(ObjectType):
    id = String()
    name = String()
    steamId = String()
    created = String()
    edited = String()

class Tournament(ObjectType):
    id = String()
    name = String()
    created = String()
    edited = String()
    maxParticipants = Int()
    minParticipants = Int()
    # participants = graphene.Field(User)
    participants = String()

class UsersList(graphene.Connection):
    class Meta:
        node = User

class TournamentList(graphene.Connection):
    class Meta:
        node = Tournament
