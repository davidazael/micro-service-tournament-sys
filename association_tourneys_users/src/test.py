import copy
import pprint as pp
import json
import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

base_url = "http://localhost/users/graphql"
# base_url_tourneys = "http://localhost/users/graphql"
headers = {'content-type': 'application/json'}
# headers = {'content-type': 'application/graphql'}
payload = '{"query": "{usersList{edges{node{id name steamId}}}}"}'
# response = requests.post(base_url, headers=headers, data=payload)
# response = requests.post(base_url_tourneys, headers=headers, data=payload)
# print(response)
# print(json.dumps(response.json(), indent=2))
# j_str = json.dumps(response.json())
# dic = json.loads(j_str)
# pp.pprint(dic, indent=2)
# print("gql \.")


_transport = RequestsHTTPTransport( url='http://localhost/users/graphql', use_json=True,)

client = Client( transport=_transport, fetch_schema_from_transport=False,)

# query_two = gql(""" { { user(id: \\"VXNlcjox\\"){ id name steamId created edited } } } """)

query_one = gql("""
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
response = client.execute(query_one)
parsed_response = response['usersList']

pp.pprint(parsed_response)
