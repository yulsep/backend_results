from flask import Blueprint
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_controller', __name__)
vote_controller = VoteController()


@vote_blueprints.route('/vote', methods=['GET'])
def index():
    """
    This method get a vote list
    :return:
    """
    return vote_controller.index()


@vote_blueprints.route('/vote/<id_>', methods=['GET'])
def show(id_: str):
    """
    This method get a vote by id
    :param id_:
    :return:
    """
    return vote_controller.show(id_)


@vote_blueprints.route('/vote', methods=['POST'])
def create():
    """
    This method create a vote
    :return:
    """
    return vote_controller.create(request.json)


@vote_blueprints.route('/vote/<id_>', methods=['PUT'])
def update(id_: str):
    """
    This method update a vote
    :param id_:
    :return:
    """
    return vote_controller.update(id_, request.json)


@vote_blueprints.route('/vote/<id_>', methods=['DELETE'])
def delete(id_: str):
    """
    This method delete a vote
    :param id_:
    :return:
    """
    return vote_controller.delete(id_)


