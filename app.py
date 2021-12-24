import os
from flask import Flask
from logging.config import dictConfig
from routes.pile import pile_endpoint

# Global 
PORT = os.environ.get('PORT')
PREFIX = os.environ.get('PREFIX')
APP = Flask(__name__)

# Default configuration
def setup():
    dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        'datefmt' : "%Y-%m-%d %H:%M:%S"
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# Run webserver
def run(app):
    app.logger.info('Launching webserver') 
    app.run(debug=True, port=PORT)

# Load endpoints
def register(app):
    app.logger.info('Registering endpoints') 
    app.register_blueprint(pile_endpoint, url_prefix=PREFIX)

if __name__ == '__main__':
    # Set default configuration
    setup()
    # Register endpoints
    register(APP)
    # Launch webserver
    run(APP)