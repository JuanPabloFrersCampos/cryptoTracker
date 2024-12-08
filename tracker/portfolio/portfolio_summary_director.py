from typing import List, Dict, LiteralString
from tracker.abstractModels.operation_model import OperationModel
from tracker.abstractModels.portfolio_summary_model import PortfolioSummaryModel
from tracker.portfolio.symbol_summary_builder import SymbolSummaryBuilder

class PortfolioSummaryDirector:
    def __init__(self, operations_grouped_by_symbol:  Dict[str, List[OperationModel]]):
        self.__operations_grouped_by_symbol = operations_grouped_by_symbol

    def process(self) -> PortfolioSummaryModel:
        portfolioSummary = PortfolioSummaryModel()
        symbols_summary_dict = {}
        totalBalance = 0
        for symbol, operations_set in self.__operations_grouped_by_symbol.items():
            symbol_summary = SymbolSummaryBuilder(symbol, operations_set)
            symbol_summary = symbol_summary.process()
            if symbol_summary.get_current_balance == "Non available": # esto no es resp de la clase
                continue
            totalBalance += symbol_summary.get_current_balance()
            symbols_summary_dict[symbol] = symbol_summary
            
        portfolioSummary.set_symbols_summary(symbols_summary_dict)
        portfolioSummary.set_total_balance(round(totalBalance, 2))
        return portfolioSummary