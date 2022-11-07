from models.vote import Vote
from repositories.vote_repository import VoteRepository


class VoteController:
    # constructor
    def __init__(self):
        print("Vote controller ready")
        self.vote_repository = VoteRepository()

    def index(self) -> list:
        """
        This method get a vote list
        :return:
        """
        print("Get all")
        return self.vote_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")
        return self.vote_repository.find_by_id(id_)

    def create(self, vote_: dict) -> dict:
        """

        :param vote_:
        :return:
        """
        print("Insert")
        vote = Vote(vote_)
        return self.vote_repository.save(vote)

    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        print("Update")
        vote = Vote(vote_)
        return self.vote_repository.update(id_, vote)

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete")
        return self.vote_repository.delete(id_)
