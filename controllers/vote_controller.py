from models.vote import Vote
from models.table import Table
from models.candidates import Candidates
from repositories.vote_repository import VoteRepository
from repositories.table_repository import TableRepository
from repositories.candidates_repository import CandidatesRepository


class VoteController:
    # constructor
    def __init__(self):
        print("Vote controller ready")
        self.vote_repository = VoteRepository()
        self.table_repository = TableRepository()
        self.candidate_repository = CandidatesRepository()

    def index(self) -> list:
        """
        This method get a vote list
        :return:
        """
        return self.vote_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.vote_repository.find_by_id(id_)

    def create(self, vote_: dict, table_id: str, candidate_id: str) -> dict:
        """

        :param candidate_id:
        :param table_id:
        :param vote_:
        :return:
        """
        vote = Vote(vote_)
        candidate_dict = self.candidate_repository.find_by_id(candidate_id)
        candidate_obj = Candidates(candidate_dict)
        table_dict = self.table_repository.find_by_id(table_id)
        table_obj = Table(table_dict)
        vote.candidate = candidate_obj
        vote.table = table_obj
        return self.vote_repository.save(vote)

    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        vote = Vote(vote_)
        return self.vote_repository.update(id_, vote)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        return self.vote_repository.delete(id_)
