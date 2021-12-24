import os
from flask import Flask
from flask import request
from models.Pile import Pile
from routes.pile import pile_endpoint

# Global 
PORT = os.environ.get('PORT')
PREFIX = os.environ.get('PREFIX')
APP = Flask(__name__)

# Run webserver
def run(app):
    app.run(debug=True, port=PORT)

# Load endpoints
def register(app):
    print("Register bluePrint")
    app.register_blueprint(pile_endpoint, url_prefix=PREFIX)

if __name__ == '__main__':
    # Register endpoints
    register(APP)
    # Launch webserver
    run(APP)