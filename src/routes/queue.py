from flask import Blueprint, request, abort
from models.Queue import Queue

# Declare Blueprint
queue_endpoint = Blueprint("queue_endpoint", __name__)

# Route default path
ENDPOINT = '/queue'

# In memory Pile
queue = Queue()

@queue_endpoint.route(ENDPOINT, methods = ['GET', 'POST', 'DELETE'])
def queu() :
    pass