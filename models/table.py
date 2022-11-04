from models.abstract_model import AbstractModel
from abc import ABC, abstractmethod


class Table(AbstractModel):

    def __init__(self, data: dict):
        super().__init__(data)
        self._id = data['_id']
        self.name = data['name']
        self.description = data['description']
        self.status = data['status']
        self.__dict__ = data

    def __str__(self):
        return f"Table: {self.name}"

    def __repr__(self):
        return f"Table: {self.name}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, item):
        return item in self.__dict__

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __delattr__(self, item):
        del self.__dict__[item]

    def __getattribute__(self, item):
        return self.__dict__[item]

