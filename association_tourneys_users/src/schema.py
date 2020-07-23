import pprint as pp
import copy
import json
import requests
from graphql import GraphQLSchema, build_client_schema
import graphene
from graphene import Connection, JSONString, relay, Field, ObjectType, Schema, String, List, Boolean, Int
from . import utils
from . import schema_associations
from . import client
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


class Query(ObjectType):
    node = relay.Node.Field()

    # Assign 'users_list' the Schema.UsersList which means it must meet the 
    # parameters that are listed in the schema.
    # users_list = relay.Node.Field(schema_associations.UsersList)
    users_list = Field(schema_associations.UsersList) 
    tournament_list = graphene.Field(schema_associations.TournamentList) 

    def resolve_users_list(self, info, *args):
        results = utils.get_user_list_client()
        return results

    def resolve_tournament_list(self, info, *args):
        results = utils.get_tournament_list()
        return results


    

schema = Schema(query=Query)
