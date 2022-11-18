from flask import Blueprint
from controllers.reports_controller import ReportController

report_blueprints = Blueprint('report_blueprints', __name__)
reports_controller = ReportController()


@report_blueprints.route("/reports/votes_by_candidate", methods=['GET'])
def get_votes_by_candidate():
    response = reports_controller.get_votes_by_candidate()
    return response, 200


@report_blueprints.route("/reports/candidates_by_tables", methods=['GET'])
def get_votes_by_table():
    response = reports_controller.get_votes_by_table()
    return response, 200


@report_blueprints.route("/reports/votes_by_political_party", methods=['GET'])
def get_votes_by_political_party():
    pass


@report_blueprints.route("/reports/percentage votes_parties", methods=['GET'])
def get_political_party_percentage_votes():
    pass

