from escavador.resources.helpers.endpoint import Endpoint
from typing import Dict

class Movimentacao(Endpoint):

    def __init__(self):
        super().__init__(api_version=1)

    def por_id(self, id_movimentacao: int) -> Dict:
        """
        Retorna uma movimentação pelo seu identificador
        :param id_movimentacao: o ID da movimentação
        :return: Dict
        """
        return self.methods.get(f"movimentacoes/{id_movimentacao}")