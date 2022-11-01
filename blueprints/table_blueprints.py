from flask import Blueprint
from flask import request

from controllers.table_controller import TableController

table_blueprints = Blueprint('table_controller', __name__)
table_controller = TableController()
