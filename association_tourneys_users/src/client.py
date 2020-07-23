import copy
import pprint as pp
import json
import requests
from . import schema_associations
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def client_call():
    _transport = RequestsHTTPTransport( url='http://api_gateway/users/graphql', use_json=True,)

    client = Client( transport=_transport, fetch_schema_from_transport=False,)

    query = gql("""
    { usersList 
        { edges 
          { node 
            { id
              name
              steamId
              created
              edited
            }
          }
        }
    }
    """)
    response = client.execute(query)
    parsed_response = response['usersList']['edges']
    size = len(parsed_response[1].get('node'))
    
    return response

def client_call():
    _transport = RequestsHTTPTransport( url='http://api_gateway/tourneys/graphql', use_json=True,)

    client = Client( transport=_transport, fetch_schema_from_transport=False,)

    query = gql("""
    { tournamentList
        { edges 
          { node 
            { id
              name
              created
              edited
              maxParticipants
              minParticipants
            }
          }
        }
    }
    """)
    response = client.execute(query)
    
    return response

