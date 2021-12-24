from flask import Blueprint, request
pile_endpoint = Blueprint("pile_endpoint", __name__)

# Route default path
ENDPOINT = '/pile'

@pile_endpoint.route(ENDPOINT, methods = ['GET', 'POST', 'DELETE'])
def pile() :
    if request.method == 'POST':
        # Retrieve data
        item = request.get_json(force=True)['item']
        pile.push(item)

    return pile.get()