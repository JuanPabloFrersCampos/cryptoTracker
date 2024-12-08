from typing import List, Dict
from tracker.abstractModels.operation_model import OperationModel

class OperationsGrouperBySymbol:
    def __init__(self, operations: List[OperationModel]):
        self.operations = operations
        
    def group_operations_by_symbol(self) -> Dict[str, List[OperationModel]]:
        operationsBySymbol = {}
        for operation in self.operations:
            symbol = operation.getSymbol()
            if symbol not in operationsBySymbol:
                operationsBySymbol[symbol] = []
            operationsBySymbol[symbol].append(operation)
        return operationsBySymbol