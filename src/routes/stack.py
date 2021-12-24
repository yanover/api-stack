from flask import Blueprint, request, abort
from models.Stack import Stack

# Declare Blueprint
stack_endpoint = Blueprint("stack_endpoint", __name__)

# Route default path
ENDPOINT = '/stack'

# In memory Pile
stack = Stack()

@stack_endpoint.route(ENDPOINT, methods = ['GET', 'POST', 'DELETE'])
def stack() :
    # Return last item
    if request.method == 'GET':
        return str(stack.get())
    # Stack item
    if request.method == 'POST':
        item = request.get_json(force=True)['item']
        if(isinstance(item, int)):
            return str(stack.push(item))
        else:
            abort(404)
    # Delete item
    elif request.method == 'DELETE':
        stack.remove()
    # Default return value    
    return ""

@stack_endpoint.route(f"{ENDPOINT}/max", methods = ['GET'])
def max() :
    return str(stack.max())

@stack_endpoint.route(f"{ENDPOINT}/min", methods = ['GET'])
def min() :
    return str(stack.max())

