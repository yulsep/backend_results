import json

import certifi
from typing import TypeVar, Generic, get_args

import pymongo

T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __init__(self):
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tslCAFile=ca
        )
        self.data_base = client[data_config.get("db-name")]
        # get generic class name
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self) -> dict:
        """

        :return:
        """
        with open("config.json", "r") as config:
            data =json.load(config)
        return data

    def find_all(self) -> list:
        """

        :return:
        """
        pass

    def fin_by_id(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        pass

    def save(self, item: T) -> T:
        """

        :param item:
        :return:
        """
        pass

    def update(self, id_: str, item: T) -> dict:
        """

        :param id_:
        :param item:
        :return:
        """
        pass

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        pass

    def query(self, query: dict) -> list:
        """

        :param query:
        :return:
        """
        pass

    def query_aggregation(self, query: dict) -> list:
        """

        :param query:
        :return:
        """
        pass

    def get_values_db_ref(self):
        """

        :return:
        """
        pass

    def get_values_db_ref_from_list(self):
        """

        :return:
        """
        pass

    def transform_object_ids(self):
        """

        :return:
        """
        pass

    def transform_refs(self):
        """

        :return:
        """
        pass

    def format_list(self):
        """

        :return:
        """
        pass

    def object_to_db_ref(self):
        """

        :return:
        """
        pass
