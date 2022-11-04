from models.political_party import PoliticalParty
from repositories.political_party_repository import PoliticalPartyRepository


class PoliticalPartyController:
    # constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("Political party controller ready")
        self.political_party_repository = PoliticalPartyRepository

    def index(self) -> list:
        """
        This method gets all political parties into the DB
        :return: political parties list
        """
        print("Get all")
        return self.political_party_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        This method get a political party by id
        :param id_:
        :return:political party
        """
        print("Show by id")

    # INSERT political party
    def create(self, political_party_: dict) -> dict:
        """
        This method insert one political party into DB
        :param political_party_:
        :return: political party´s dictionary
        """
        print("Insert")
        political_party = PoliticalParty(political_party_)
        return self.political_party_repository.save(political_party)

    # UPDATE political party
    def update(self, id_: str, political_party_: dict) -> dict:
        """
        This method update the political parties
        :param id_: id_
        :param political_party_:
        :return: political party´s dictionary
        """
        print("Update")
        political_party = PoliticalParty(political_party_)
        return self.political_party_repository.update(id_, political_party)

    # DELETE one political party
    def delete(self, id_: str) -> str:
        """
        This Method  delete a Political Party by ID
        :param id_: id of political party to delete
        :return: Nothing
        """
        print("Delete" + id_)
        return self.political_party_repository.delete(id_)


