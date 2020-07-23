#!/usr/bin/env python3.7
from .database.base import db_session
from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.add_url_rule(
        '/users/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/users/')
def index():
    return "<span style='color:red'>I am app 1</span>"

@app.route('/users/hello')
def hello():
    return 'hello, world!'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__=="__main__":
    app.run(threaded=True)
