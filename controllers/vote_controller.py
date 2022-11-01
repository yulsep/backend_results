from models.vote import Vote


class   VoteController:
    # constructor
    def __init__(self):
        print("Vote controller ready")

    def index(self) -> list:
        """
        This method get a vote list
        :return:
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    def create(self, vote_: dict) -> dict:
        """

        :param vote_:
        :return:
        """
        print("Insert")

    def update(self, id_: str, vote_: dict) -> dict:
        """

        :param id_:
        :param vote_:
        :return:
        """
        print("Update")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete")
