from flask import Blueprint

second = Blueprint('second', __name__, url_prefix='/second')


@second.route('/')
def show():
    return "hello world flask autoreload"
