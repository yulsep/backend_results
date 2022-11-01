from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_controller', __name__)
vote_controller = VoteController()
