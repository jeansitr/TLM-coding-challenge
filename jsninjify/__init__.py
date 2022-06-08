from flask import Flask, app, jsonify, redirect, request
from flask.wrappers import Response
from jsninjify.models import init_app

def create_app(initial_config=None):
    app = Flask("jsninjify", template_folder="templates")
    init_app(app)

    #importing routes within the app's context
    with app.app_context():
        import jsninjify.routes

        return app