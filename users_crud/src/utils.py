from graphql_relay.node.node import from_global_id


def input_to_dict(input):
    """ Method to convert Graphene input into dictionary."""
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key[-2:] == 'id' and input[key] != 'unknown':
            input[key] = from_global_id(input[key])[1]
        dictionary[key] = input[key]
    return dictionary

def input_to_dict_int(input, key_value):
    """ Method to convert Graphene input of key_value into dictionary int."""
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key == key_value:
            input[key] = from_global_id(input[key])[1]
        dictionary[key] = input[key]
    return dictionary
