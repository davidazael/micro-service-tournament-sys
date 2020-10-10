import copy
import json
import requests
import collections
from graphql_relay.node.node import from_global_id
from graphql.execution.base import collect_fields
from graphql.utils.ast_to_dict import ast_to_dict
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def my_get_fields(info):
    prev_fragment_names = set()
    params = collections.defaultdict(list)
    params = collect_fields(info.context,
            info.parent_type,
            info.field_asts[0].selection_set,
            params,
            prev_fragment_names)
    params = collect_fields(info.context,
            info.parent_type,
            params['edges'][0].selection_set,
            params,
            prev_fragment_names)
    params = collect_fields(info.context,
            info.parent_type,
            params['node'][0].selection_set,
            params,
            prev_fragment_names)
    return set(params)


def get_fields(info):
    prev_fragment_names = set()
    params = collections.defaultdict(list)
    params = collect_fields(info.context,
            info.parent_type,
            info.field_asts[0].selection_set,
            params,
            prev_fragment_names)
    prev_fragment_names = set(params.keys())
    for fragment_name in prev_fragment_names:
        params = collect_fields(info.context,
                info.parent_type,
                params[fragment_name][0].selection_set,
                params,
                prev_fragment_names)
        prev_fragment_names = set(params.keys())

    return set(params)

def test_collect_fields(node, fragments):
    """Recursively collects fields from the AST
    Args:
        node (dict): A node in the AST
        fragments (dict): Fragment definitions
    Returns:
        A dict mapping each field found, along with their sub fields.
        {'name': {},
         'sentimentsPerLanguage': {'id': {},
                                   'name': {},
                                   'totalSentiments': {}},
         'slug': {}}
    """
    field = {}

    if node.get('selection_set'):
        for leaf in node['selection_set']['selections']:
            if leaf['kind'] == 'Field':
                field.update({
                    leaf['name']['value']: test_collect_fields(leaf, fragments)
                })
            elif leaf['kind'] == 'FragmentSpread':
                field.update(test_collect_fields(fragments[leaf['name']['value']],
                                            fragments))

    return field


def test(info):
    """A convenience function to call collect_fields with info
    Args:
        info (ResolveInfo)
    Returns:
        dict: Returned from collect_fields
    """
    prev_fragment_names = set()
    fragments = {}
    node = ast_to_dict(info.field_asts[0])
    for name, value in info.fragments.items():
        fragments[name] = ast_to_dict(value)

    return test_collect_fields(node, fragments)

def _json_object_hook(d):
    return collections.namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

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
    app_url = 'http://api_gateway/users/graphql'
    try:
        import os
        app_url = 'http://'+os.environ['URL']+'/users/graphql?'
    except KeyError as e:
        print("No URL Set")
        app_url = 'http://api_gateway/users/graphql'

    _transport = RequestsHTTPTransport( url=app_url, use_json=True,)
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
    app_url = 'http://api_gateway/tourneys/graphql'
    try:
        import os
        app_url = 'http://'+os.environ['URL']+'/tourneys/graphql?'
    except KeyError as e:
        print("No URL Set")
        app_url = 'http://api_gateway/tourneys/graphql'

    _transport = RequestsHTTPTransport( url=app_url, use_json=True,)

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


def requests_all_tourneys(info):
    vals = test(info)
    vals = set(vals['edges']['node'].keys())
    headers = {'content-type': 'application/json'}
    base_url = 'http://api_gateway/tourneys/graphql'
    payload = '{"query": "{tournamentList {edges {node { {} {} {} {} {} }}}}"}'.format(
        *vals)
    tournament_response = requests.post(url=base_url, headers=headers, data=payload)
    parsed_response = tournament_response['tournamentList']
    return parsed_response


def request_from_tournament(found_id):
    headers = {'content-type': 'application/json'}
    base_url = 'localhost:5000/tourneys/graphql'
    payload = '{"query": "{tournament(tournament_id:{0.found_id}){tournament{name,owner}}}"}'.format(
        found_id)
    tournament_response = requests.post(
        url=base_url, headers=headers, data=payload)
    print(tournament_response.json())
    return tournament_response
