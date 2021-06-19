from user import User
from flask import Flask
from flask import Blueprint
from flask_restful import Api, Resource
from user import User

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    
    api.add_resource(User, '/Hello')
    app.register_blueprint(api_bp, url_prefix='/api')

    #from Model import db
    #db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)