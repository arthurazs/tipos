from enum import Enum
import typing

class TipoTransformador(Enum):
    OLEO = 0
    SECO = 1

class Transformador:

    # dunder = double underscore
    def __init__(self, identificacao: typing.Union[str, int], tipo: int, valor: typing.Any):
        self.identificacao = identificacao
        self._tipo = TipoTransformador(tipo)
        if tipo == 1:
            self._status = "Ok"
        else:
            self._status = "Error"
        self.valor = valor

    @property
    def tipo(self) -> str:
        return self._tipo.name

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> bool:
        if self._tipo == TipoTransformador(1):
            self._status = value
            return True
        return False

