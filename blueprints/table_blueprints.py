from flask import Blueprint, jsonify
from flask import request

from controllers.table_controller import TableController

table_blueprints = Blueprint('table_controller', __name__)
table_controller = TableController()


@table_blueprints.route('/table/all', methods=['GET'])
def get_all_tables():
    """
    This method get a table list
    :return:
    """
    response = table_controller.index()
    return jsonify(response), 200


@table_blueprints.route('/table/<string:id_>', methods=['GET'])
def get_table_by_id(id_: str):
    """
    :param id_:
    :return:
    """
    response = table_controller.show(id_)
    return jsonify(response), 200


@table_blueprints.route('/table/save', methods=['POST'])
def table_insert():
    """
    :return:
    """
    table_ = request.get_json()
    response = table_controller.create(table_)
    return jsonify(response), 201


@table_blueprints.route('/table/update/<string:id_>', methods=['PATCH'])
def table_update(id_: str):
    """
    :param id_:
    :return:
    """
    table_ = request.get_json()
    response = table_controller.update(id_, table_)
    return jsonify(response), 201


@table_blueprints.route('/table/delete/<string:id_>', methods=['DELETE'])
def table_delete(id_: str):
    """
    :param id_:
    :return:
    """
    response = table_controller.delete(id_)
    return jsonify(response), 204


