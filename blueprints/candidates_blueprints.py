from flask import Blueprint, jsonify
from flask import request

from controllers.candidates_controller import CandidateController

candidate_blueprints = Blueprint('candidate_blueprints', __name__)
candidate_controller = CandidateController()


@candidate_blueprints.route("/candidate/all", methods=["GET"])
def get_all_candidates():
    response = candidate_controller.index()
    return jsonify(response), 200


@candidate_blueprints.route("/candidate/<string:id_>", methods=["GET"])
def get_candidates_by_id(id_):
    response = candidate_controller.show()
    return jsonify(response), 200


@candidate_blueprints.route("/candidate/insert", methods=["POST"])
def candidate_insert():
    candidate = request.get_json()
    response = candidate_controller.create(candidate)
    return jsonify(response), 201


@candidate_blueprints.route("/candidate/update/<string:id_>", methods=["PATH"])
def candidate_update(id_):
    candidate = request.get_json()
    response = candidate_controller.update(id_, candidate)
    return jsonify(response), 201


@candidate_blueprints.route("/candidate/delete/<string:id_>", methods=["DELETE"])
def candidate_delete(id_):
    response = candidate_controller.delete(id_)
    return jsonify(response), 204
