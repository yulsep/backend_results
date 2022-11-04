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
        data ={
            "id": 1,
            "name": "Mesa 1",
            "description": "Mesa 1",
            "status": "Activo"
        }
        table = Table(data)

    def show(self, id_: str) -> dict:
        """
        :param id_:
        :return:
        """
        print("Show by id")
        data ={
            "_id": id_,
            "name": "Mesa 1",
            "description": "Mesa 1",
            "status": "Activo"
        }
        table = Table(data)

    def create(self, table_: dict) -> dict:
        """

        :param table_:
        :return:
        """
        print("Insert")
        table = Table(table_)
        return table.__dict__



    def update(self, id_: str, table_: dict) -> dict:
        """

        :param id_:
        :param table_:
        :return:
        """
        print("Update")
        data = table_
        data["_id"] = id_
        table = Table(table_)
        return table.__dict__

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("Delete" + id_)
        return ("Delete count: " + id_)
