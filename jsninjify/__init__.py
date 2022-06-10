from flask import Flask
from jsninjify.models import init_app

def create_app(initial_config=None):
    app = Flask("jsninjify", template_folder="templates")
    init_app(app)
    app.config['UPLOAD_FOLDER'] = "./upload"


    #importing routes within the app's context
    with app.app_context():
        import jsninjify.routes

        return app