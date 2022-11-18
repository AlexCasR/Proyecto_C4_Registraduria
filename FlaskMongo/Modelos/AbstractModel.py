from abc import ABCMeta

class AbstractModel(metaclass=ABCMeta):
    def __init__(self, data):
        for clave, valor in data.items():
            setattr(self, clave, valor)