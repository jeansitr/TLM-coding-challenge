from flask import Flask, app, jsonify, redirect, request
from flask.wrappers import Response

def create_app(initial_config=None):
    app = Flask("jsninjify", template_folder="templates")

    #importing routes within the app's context
    with app.app_context():
        import jsninjify.routes

        return app