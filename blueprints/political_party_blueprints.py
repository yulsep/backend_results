from flask import Blueprint, jsonify
from flask import request

from controllers.political_party_controller import PoliticalPartyController

political_party_blueprints = Blueprint('political_party_controller', __name__)
political_party_controller = PoliticalPartyController()


@political_party_blueprints.route("/political_parties/all", methods=["GET"])
def get_all_political_parties():
    response = political_party_controller.index()
    return jsonify(response), 200


@political_party_blueprints.route("/political_party/<string:id_>", methods=['GET'])
def get_political_party_by_id(id_):
    response = political_party_controller.show(id_)
    return jsonify(response), 200


@political_party_blueprints.route("/political_party/insert", methods=['POST'])
def insert_political_party():
    political_party = request.get_json()
    response = political_party_controller.create(political_party)
    return jsonify(response), 201


@political_party_blueprints.route("/political_party/update/<string:id_>", methods=['PATCH'])
def update_political_party(id_):
    political_party = request.get_json()
    response = political_party_controller.update(id_, political_party)
    return jsonify(response), 201


@political_party_blueprints.route("/political_party/delete/<string:id_>", methods=['DELETE'])
def delete_political_party(id_):
    response = political_party_controller.delete(id_)
    return jsonify(response), 204