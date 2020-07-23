from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from .database.base import db_session
from .database.model_tournaments import ModelTournaments
import graphene
from . import utils


# Creating Schema Contract for Tournaments
class TournamentAttribute:
    name = graphene.String(description="Name of Tournament.")
    max_participants = graphene.Int(description="Max number of participants.")
    min_participants = graphene.Int(description="Min number of participants.")
    list_of_participants = graphene.List(description="List of Participants Global ID")


class Tournament(SQLAlchemyObjectType):
    """Tournament Node."""
    class Meta:
        model = ModelTournaments
        interfaces = (graphene.relay.Node,)


class CreateTournamentInput(graphene.InputObjectType, TournamentAttribute):
    """Arguments for Creating a Tournament."""
    pass


class CreateTournament(graphene.Mutation):
    """Mutation for Tournament creation."""
    tournament = graphene.Field(
        lambda: Tournament, description='Tournament is created by this Mutation.')

    class Arguments:
        input = CreateTournamentInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dict(input)
        data = utils.input_to_dict_int(input, 'owner_Id')
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        tournament = ModelTournaments(**data)
        db_session.add(tournament)
        db_session.commit()
        return CreateTournament(tournament=tournament)


class UpdateTournamentInput(graphene.InputObjectType, TournamentAttribute):
    """Arguments for updating Tournament """
    id = graphene.ID(required=True, description='Global ID for User.')

class UpdateTournament(graphene.Mutation):
    """Updating Tournament """
    tournament = graphene.Field(lambda: Tournament, description='Tournament updated by this Mutation.')

    class Arguments:
        input = UpdateTournamentInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dict(input)
        data = utils.input_to_dict_int(input, 'owner_Id')
        data['edited'] = datetime.utcnow()

        tournament = db_session.query(ModelTournaments).filter_by(id=data['id'])
        tournament.update(data)
        db_session.commit()
        tournament = db_session.query(ModelTournaments).filter_by(id=data['id']).first()

        return UpdateTournament(tournament=tournament)

class DeleteTournamentInput(graphene.InputObjectType, TournamentAttribute):
    """Arguments requiered to Delete. """
    id = graphene.ID(required=True, description='Global ID for User.')

class DeleteTournament(graphene.Mutation):
    """Delete Tournament """
    tournament = graphene.Field(lambda: Tournament, description='Tournament updated by this Mutation.')

    class Arguments:
        input = DeleteTournamentInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dict(input)
        data = utils.input_to_dict_int(input, 'owner_Id')
        data['edited'] = datetime.utcnow()

        tournament = db_session.query(ModelTournaments).filter_by(id=data['id'])
        tournament.delete()
        db_session.commit()
        tournament = db_session.query(ModelTournaments).filter_by(id=data['id']).first()

        return DeleteTournament(tournament=tournament)
