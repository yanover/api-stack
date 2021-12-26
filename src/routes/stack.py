from flask import Blueprint, request, abort
from models.Stack import Stack
from common.errors.IsFullException import IsFullException

# Declare Blueprint
stack_endpoint = Blueprint("stack_endpoint", __name__)

# Route default path
ENDPOINT = '/stack'

# In memory Pile
stack = Stack()


@stack_endpoint.route(ENDPOINT, methods=['GET', 'POST', 'DELETE'])
def default():
    try:
        if request.method == 'GET':
            return str(stack.peek())
        if request.method == 'POST':
            item = request.get_json(force=True)['item']
            stack.push(item)
        elif request.method == 'DELETE':
            stack.pop()
        # Default return value
        return str(stack.__str__())
    except (TypeError, IsFull) as e:
        abort(404, description=e)

@stack_endpoint.route(f"{ENDPOINT}/max", methods=['GET'])
def max():
    return str(stack.max())


@stack_endpoint.route(f"{ENDPOINT}/min", methods=['GET'])
def min():
    return str(stack.min())
