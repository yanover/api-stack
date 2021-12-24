from flask import Blueprint, request
from models.Pile import Pile

# Declare Blueprint
pile_endpoint = Blueprint("pile_endpoint", __name__)

# Route default path
ENDPOINT = '/pile'

# Temporary
pile = Pile()

@pile_endpoint.route(ENDPOINT, methods = ['GET', 'POST', 'DELETE'])
def stack() :
    if request.method == 'GET':
        return str(pile.get())

    if request.method == 'POST':
        # Retrieve data
        item = request.get_json(force=True)['item']
        
        if(isinstance(item, int)):
            return str(pile.push(item))
        else:
            print(f"{item} is not an integer")            

    if request.method == 'DELETE':
        return pile.delete()
    
    return ""

