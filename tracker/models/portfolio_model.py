from models import OperationModel
from typing import List
from django.db.models.query import QuerySet

class PortfolioModel:

    def __init__(self): # obtener operations con el dao y haciendo new operationModel
        self.__name = None
        self.__operations = None

    @classmethod
    def from_db(cls, name: str, operations: QuerySet):
        operations = [
            OperationModel(
                symbol=operation.symbol,
                assetQuantity=operation.assetQuantity,
                price=operation.price,
                isSell=operation.isSell
            )
            for operation in operations
        ]
        return cls(name, operations)
    
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def set_operations(self, operations: List[OperationModel]):
        self.__operations = operations

    def get_operations(self) -> List[OperationModel]:
        return self.__operations
