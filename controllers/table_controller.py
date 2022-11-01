from models.table import Table


class TableController:
    # constructor
    def __init__(self):
        print("Table controller ready")

    def index(self) -> list:
        """
        This method get a table list
        :return:
        """
        print("Get all")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("Show by id")

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert")

    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete")
