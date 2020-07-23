from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
from . import schema_users

class Query(graphene.ObjectType):
    """ Nodes which can be Queried by this API. """
    node = graphene.relay.Node.Field()

    # Users
    user = graphene.relay.Node.Field(schema_users.User)
    users_list = SQLAlchemyConnectionField(schema_users.User)

class Mutation(graphene.ObjectType):
    """ Mutations which can be performed by this API. """
    # User Mutation
    create_user = schema_users.CreateUser.Field()
    update_user = schema_users.UpdateUser.Field()
    delete_user = schema_users.DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
