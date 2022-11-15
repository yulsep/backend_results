from flask import Blueprint
from controllers.reports_controller import ReportController

report_blueprints = Blueprint('report_blueprints', __name__)
report_controller = ReportController()


@report_blueprints.route("/reports/votes_by_candidate", methods=['GET'])
def votes_by_candidate():
    response = report_controller.get_votes()
    return response, 200

