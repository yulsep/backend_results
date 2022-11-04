from models.political_party import PoliticalParty


class PoliticalPartyController:
    # constructor
    def __init__(self):
        print("Political party controller ready")

    def index(self) -> list:
        """
        This method get a political party list
        :return:
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """
        This method get a political party by id
        :param id_:
        :return:political party
        """
        print("Show by id")

    def create(self, political_party_: dict) -> dict:
        """

        :param political_party_:
        :return:
        """
        print("Insert")

    def update(self, id_: str, political_party_: dict) -> dict:
        """

        :param id_:
        :param political_party_:
        :return:
        """
        print("Update")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete")
