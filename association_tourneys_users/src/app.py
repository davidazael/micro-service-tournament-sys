#!/usr/bin/env python3.7
from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema
from . import utils


def graphql_view():
    view = GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True)

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.add_url_rule(
        '/assoc/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/assoc/')
def index():
    return utils.get_user_list()
    # return "<span style='color:red'>I am the AssociationTourneysUsers App</span>"

@app.route('/assoc/hello')
def hello():
    return 'hello, world!'

if __name__=="__main__":
    app.run(threaded=True)
