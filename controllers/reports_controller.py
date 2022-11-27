from repositories.report_repository import ReportRepository


class ReportController:
    def __init__(self):
        self.report_repository = ReportRepository()

    # get reports by candidates
    def get_votes_in_candidate(self, id_candidate):
        return self.report_repository.get_votes_in_candidate(id_candidate)

    def get_votes_by_candidate(self):
        return self.report_repository.get_vote_by_candidate()

    # get reports by tables
    def get_votes_by_table(self):
        return self.report_repository.get_votes_by_table()

    def get_votes_in_table(self, table_id):
        return self.report_repository.get_votes_in_table(table_id)

    # get reports by political party
    def get_votes_by_political_party(self):
        return self.report_repository.get_votes_by_political_party()

    def get_political_party_percentage_votes(self):
        return self.report_repository.get_political_party_percentage_votes()
