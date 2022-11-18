from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
    # constructor
    def __init__(self, data: dict):
        # items convierte el diccionario en un listado de tuplas clave valor
        for key, value in data.items():
            setattr(self, key, value)
