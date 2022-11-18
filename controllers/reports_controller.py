from repositories.report_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_votes_by_candidate(self):
        return self.report_repository.get_votes_by_candidate()

    def get_votes_by_table(self):
        return self.report_repository.get_votes_by_table()
