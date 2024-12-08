from typing import List, LiteralString
from tracker.abstractModels.symbol_summary_model import SymbolSummaryModel
from tracker.abstractModels.operation_model import OperationModel
from tracker.externalCryptoPriceFetcher import ExternalCryptoPriceFetcher

class SymbolSummaryBuilder:
    def __init__(self, symbol: LiteralString, operations_set: List[OperationModel]):
        self.__symbol = symbol
        self.__operations_set = operations_set
        self.__symbol_summary_model = SymbolSummaryModel()
        self.__holdings = None
        self.__total_cost = None
        self.__total_proceeds = None
        self.__symbol_market_price = None
        self.__current_balance = None

    def process(self) -> SymbolSummaryModel:
        self.set_holdings()
        self.set_total_cost_and_proceeds()
        self.set_symbol_market_price()
        self.set_holdings_value()
        self.set_current_balance()
        return self.__symbol_summary_model

    def set_holdings(self):
        holdings = 0
        for operation in self.__operations_set:
            if operation.isSell:
                holdings -= operation.assetQuantity
            else:
                holdings += operation.assetQuantity
        self.__holdings = (round(holdings, 4))
        self.__symbol_summary_model.set_holdings(round(holdings, 4))

    def set_total_cost_and_proceeds(self):
        total_cost = 0
        proceeds = 0
        holdings = 0
        for operation in self.__operations_set:
            if operation.isSell:
                costPerUnit = total_cost / holdings if holdings > 0 else 0
                total_cost -= costPerUnit * operation.assetQuantity
                proceeds += operation.assetQuantity * operation.price
                holdings -= operation.assetQuantity
            else:
                total_cost += operation.assetQuantity * operation.price
                holdings += operation.assetQuantity
        self.__symbol_summary_model.set_total_cost(round(total_cost, 2))
        self.__symbol_summary_model.set_total_proceeds(round(proceeds, 2))
        self.__total_cost = round(total_cost, 2)
        self.__total_proceeds = round(proceeds, 2)

    def set_symbol_market_price(self):
        externalCryptoPriceFetcher = ExternalCryptoPriceFetcher(symbol = self.__symbol)
        self.__symbol_summary_model.set_symbol_market_price(round(externalCryptoPriceFetcher.getPrice(), 2))
        self.__symbol_market_price = round(externalCryptoPriceFetcher.getPrice(), 2)

    def set_holdings_value(self):
        self.__symbol_summary_model.set_holdings_value(round(self.__holdings * self.__symbol_market_price, 2))

    def set_current_balance(self):
        if not self.__symbol_market_price:
            self.__symbol_summary_model.set_current_balance("Non available") # arreglar
        currentValue = float(self.__holdings) * float(self.__symbol_market_price)
        self.__symbol_summary_model.set_current_balance(round(currentValue + self.__total_proceeds - self.__total_cost, 2))

    def get_operations_set(self):
        return self.__operations_set

    def get_holdings(self):
        return self.__holdings

    def get_total_cost(self):
        return self.__total_cost

    def get_total_proceeds(self):
        return self.__total_proceeds

    def get_symbol_market_price(self):
        return self.__symbol_market_price

    def get_current_balance(self):
        return self.__current_balance