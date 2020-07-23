from graphene import SelectionSet, Selection
import graphene

def resolve_tourney(self, info, **kwargs):
    selection = SelectionSet([
        Selection()
        ])
