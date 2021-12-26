from flask import Blueprint, request, abort
from models.Stack import Stack
from common.errors.IsFullException import IsFullException
from flask import current_app

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
            current_app.logger.debug('PEEK request on current stack')
            return str(stack.peek())
        if request.method == 'POST':
            current_app.logger.debug('PUSH request on current stack')
            item = request.get_json(force=True)['item']
            stack.push(item)
        elif request.method == 'DELETE':
            current_app.logger.debug('POP request on current stack')
            stack.pop()
        # Default return value
        return str(stack.__str__())
    except (TypeError, IsFullException) as e:
        current_app.logger.debug(e)
        abort(404, description=e)
    except Exception as e:
        current_app.logger.debug(e)
        abort(500, description=e)


@stack_endpoint.route(f"{ENDPOINT}/max", methods=['GET'])
def max():
    return str(stack.max())


@stack_endpoint.route(f"{ENDPOINT}/min", methods=['GET'])
def min():
    return str(stack.min())
