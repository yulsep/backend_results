from repositories.report_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    def get_votes_by_candidate(self, id_candidate):
        return self.report_repository.get_votes_by_candidate(id_candidate)

    def get_votes_by_table(self):
        return self.report_repository.get_votes_by_table()

    def get_votes_by_political_party(self):
        return self.report_repository.get_votes_by_political_party()
