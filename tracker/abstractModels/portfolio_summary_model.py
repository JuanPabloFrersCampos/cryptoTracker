from typing import List, Dict
from tracker.abstractModels.symbol_summary_model import SymbolSummaryModel

class PortfolioSummaryModel:

    def __init__(self):
        self.__symbols_summary = []
        self.__total_balance = None

    def set_symbols_summary(self, summary: Dict[str, List[SymbolSummaryModel]]):
        self.__symbols_summary = summary
    
    def set_total_balance(self, total_balance: float):
        self.__total_balance = total_balance

    def get_symbols_summary(self):
        return self.__symbols_summary

    def to_dict(self):
        summary_dict = {}
        for symbol, symbol_summary in self.__symbols_summary.items():
            summary_dict[symbol] = symbol_summary.to_dict()
        return {
            'data': summary_dict,
            'total_balance': self.__total_balance
        }