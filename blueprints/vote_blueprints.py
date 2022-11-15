from flask import Blueprint, jsonify
from flask import request

from controllers.vote_controller import VoteController

vote_blueprints = Blueprint('vote_controller', __name__)
vote_controller = VoteController()


@vote_blueprints.route("/vote/all", methods=["GET"])
def get_all_vote():
    response = vote_controller.index()
    return jsonify(response), 200


@vote_blueprints.route('/vote/<string:id_>', methods=['GET'])
def get_votes_by_id(id_):
    response = vote_controller.show(id_)
    return jsonify(response), 200


@vote_blueprints.route("/vote/table/<string:table_id>/candidate/<string:candidate_id>", methods=['POST'])
def vote_insert(table_id, candidate_id):
    vote = request.get_json()
    response = vote_controller.create(vote, table_id, candidate_id)
    return jsonify(response), 201


@vote_blueprints.route("/vote/update/<string:id_>", methods=["PATCH"])
def vote_update(id_):
    vote = request.get_json()
    response = vote_controller.update(id_, vote)
    return jsonify(response), 201


@vote_blueprints.route("/vote/delete/<string:id_>", methods=["DELETE"])
def vote_delete(id_):
    response = vote_controller.delete(id_)
    return jsonify(response), 204