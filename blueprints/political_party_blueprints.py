from flask import Blueprint
from flask import request

from controllers.political_party_controller import PoliticalPartyController

political_party_blueprints = Blueprint('political_party_controller', __name__)
political_party_controller = PoliticalPartyController()
