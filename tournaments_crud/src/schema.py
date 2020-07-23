from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
from . import schema_tournaments

class Query(graphene.ObjectType):
    """ Nodes which can be Queried by this API. """
    node = graphene.relay.Node.Field()

    # Tournaments
    tournament = graphene.relay.Node.Field(schema_tournaments.Tournament)
    tournament_list = SQLAlchemyConnectionField(schema_tournaments.Tournament)

class Mutation(graphene.ObjectType):
    """ Mutations which can be performed by this API. """
    # Tournament Mutation
    create_tournament = schema_tournaments.CreateTournament.Field()
    update_tournament = schema_tournaments.UpdateTournament.Field()
    delete_tournament = schema_tournaments.DeleteTournament.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
