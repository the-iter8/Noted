from flask import Blueprint

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

from . import views, errors

