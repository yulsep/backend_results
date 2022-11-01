from flask import Blueprint
from flask import request

from controllers.candidates_controller import CandidateController

candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()
