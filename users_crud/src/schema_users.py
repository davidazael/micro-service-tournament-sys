from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from .database.base import db_session
from .database.model_users import ModelUsers
import graphene
from . import utils


# Create Generic class to mutualize description of User attributes for both queries.
class UserAttribute:
    name = graphene.String(description="Name of User.")
    # first_name = graphene.String(description="First Name of User.")
    # middle_first_name = graphene.String(description="Middle Name of User.")
    # last_name = graphene.String(description="Last Name of User.")
    steam_Id = graphene.Int(description="Steam ID of User.")
    # attending_tournament = graphene.List(description="List of Tournament Global IDs")
    # owner_tournament = graphene.List(description="List of Tournament Global ID as Owner")


class User(SQLAlchemyObjectType):
    """ User Node. """
    class Meta:
        model = ModelUsers
        interfaces = (graphene.relay.Node,)


class CreateUserInput(graphene.InputObjectType, UserAttribute):
    """ Arguments for creating users. """
    pass


class CreateUser(graphene.Mutation):
    """ Mutation for User Creation """
    user = graphene.Field(
        lambda: User, description="Person created by this Mutation.")

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dict(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        user = ModelUsers(**data)
        db_session.add(user)
        db_session.commit()
        return CreateUser(user=user)


class UpdateUserInput(graphene.InputObjectType, UserAttribute):
    """ Arguments for Updating User. """
    id = graphene.ID(required=True, description='Global ID for User.')


class UpdateUser(graphene.Mutation):
    """ Update User. """
    user = graphene.Field(
        lambda: User, description='User updated by this Mutation.')
    # steam_Id = graphene.Field(lambda: User, description="Steam ID of User.")

    class Arguments:
        input = UpdateUserInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dict(input)
        data['edited'] = datetime.utcnow()

        user = db_session.query(ModelUsers).filter_by(id=data['id'])
        user.update(data)
        db_session.commit()
        user = db_session.query(ModelUsers).filter_by(id=data['id']).first()

        return UpdateUser(user=user)

class DeleteUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments for Deleting a User """
    id = graphene.ID(required=True, description='Global ID for User.')
    name = graphene.String(required=True, description="Name of User.")

class DeleteUser(graphene.Mutation):
    """ Delete User. """
    user = graphene.Field(lambda: User, description='User updated by this Mutation.')

    class Arguments:
        input = UpdateUserInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dict(input)
        data['edited'] = datetime.utcnow()

        user = db_session.query(ModelUsers).filter_by(id=data['id'])
        user.delete()
        db_session.commit()
        user = db_session.query(ModelUsers).filter_by(id=data['id']).first()

        return DeleteUser(user=user)
