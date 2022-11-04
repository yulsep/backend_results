from models.political_party import PoliticalParty


class PoliticalPartyController:
    # constructor
    def __init__(self):
        """
        Constructor of the class
        """
        print("Political party controller ready")

    # get All political parties
    def index(self) -> list:
        """
        This method gets all political parties into the DB
        :return: political parties list
        """
        print("Get all")
        # Test code with data burned
        data = {
            "_id": "abc123",
            "name": "Henry",
            "lastname": "Escobar",
            "personal_id": "98580"
        }

    # get ONE political party
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
        # Test code with data burned
        political_party = PoliticalParty(political_party_)
        return political_party.__dict__

    # UPDATE political party
    def update(self, id_: str, political_party_: dict) -> dict:
        """
        This method update the political parties
        :param id_: id_
        :param political_party_:
        :return: political party´s dictionary
        """
        # Test code with data burned
        print("Update")
        data = political_party_
        data['_id'] = id_
        political_party_ = PoliticalParty(political_party_)
        return political_party_.__dict__

    # DELETE one political party
    def delete(self, id_: str) -> str:
        """
        This Method  delete a Political Party by ID
        :param id_: id of political party to delete
        :return: Nothing
        """
        print("Delete" + id_)
        # Test code with data burned
        return {"Delete count": 1}

