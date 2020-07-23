import copy
import json
import requests
from graphql_relay.node.node import from_global_id
from collections import namedtuple
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

def extract_nodes(info, size):
    pass


def input_to_dict(input):
    """ Method to convert Graphene input into dictionary."""
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key[-2:] == 'id' and input[key] != 'unknown':
            input[key] = from_global_id(input[key])[1]
        dictionary[key] = input[key]
    return dictionary

def get_user_list():
    list_of_dict = []
    dictionary = {}
    headers = {'content-type': 'application/json'}
    base_url = 'http://api_gateway/users/graphql'
    payload = '{"query": "{usersList{edges{node{id}}}}"}'
    users_response = requests.post(url=base_url, headers=headers, data=payload)
    
    data = json.loads(json.dumps(users_response.json()))
    parsed_response = data['usersList']['edges']
    dictionary = copy.deepcopy(parsed_response[0])
    # for x in len(parsed_response[0]):
        # dictionary = parsed_response[x].items()
        # list_of_dict.append(dictionary)

    return dictionary.values()

def get_user_list_client():
    _transport = RequestsHTTPTransport( url='http://api_gateway/users/graphql', use_json=True,)
    client = Client( transport=_transport, fetch_schema_from_transport=False,)
    query = gql("""
    {
    usersList {
                edges {
                  node {
                    id
                    name
                    steamId
                    created
                    edited
                  }
                }
              }
    }
    """)
    # params = *args
    response = client.execute(query)
    # parsed_response = response['usersList']['edges']
    parsed_response = response['usersList']
    # size = len(parsed_response[1].get('node'))
    dictionary = {} 
    # dictionary = copy.deepcopy(parsed_response[0])
    dictionary = copy.deepcopy(parsed_response)

    return parsed_response

def get_tournament_list():
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
    parsed_response = response['tournamentList']

    return parsed_response



def get_user():
    _transport = RequestsHTTPTransport( url='http://api_gateway/users/graphql', use_json=True,)
    client = Client( transport=_transport, fetch_schema_from_transport=False,)
    query = gql("""
    {
    { user(id: \\"VXNlcjox\\"){ id name steamId created edited } } 
    }
    """)
    response = client.execute(query)
    parsed_response = response['usersList']['edges']
    size = len(parsed_response[1].get('node'))
    dictionary = {} 
    dictionary = copy.deepcopy(parsed_response[0])

    return dictionary


def get_data_from_ids(input):
    dictionary = {}

    for key, value in input:
        print(key, value)
        if key == 'tournament_id':
            tournament_response = request_from_tournament(value)
        if key == 'user_id':
            users_response = request_from_user(value)

    return tournament_response, users_response


def request_from_user(found_id):
    headers = {'content-type': 'application/json'}
    base_url = 'localhost:5000/users/graphql'
    payload = '{"query": "{tournament(tournament_id:{0.found_id}){tournament{name,owner}}}"}'.format(
        found_id)
    users_response = requests.post(url=base_url, headers=headers, data=payload)
    print(users_response.json())
    return users_response


def request_from_tournament(found_id):
    headers = {'content-type': 'application/json'}
    base_url = 'localhost:5000/tourneys/graphql'
    payload = '{"query": "{tournament(tournament_id:{0.found_id}){tournament{name,owner}}}"}'.format(
        found_id)
    tournament_response = requests.post(
        url=base_url, headers=headers, data=payload)
    print(tournament_response.json())
    return tournament_response
