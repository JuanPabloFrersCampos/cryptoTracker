from django.http import HttpResponse, HttpRequest
from tracker.dao import Dao
from tracker.abstractModels.portfolio_model import PortfolioModel
from tracker.portfolio.symbol_summary_builder import SymbolSummaryBuilder
from tracker.abstractModels.portfolio_summary_model import PortfolioSummaryModel
from tracker.portfolio.operations_grouper_by_symbol import OperationsGrouperBySymbol
from tracker.portfolio.portfolio_summary_builder import PortfolioSummaryBuilder

class PortfolioEndpointHandler:
    def __init__(self, request: HttpRequest):
        self.request = request # en el futuro solo recibe request, se consiguen requests x user
        dao = Dao()
        portfolioModel = PortfolioModel()
        self.__portfolio = portfolioModel.from_db(name='testPortfolio', operations=dao.get_user_portfolio())
        self.__operations_grouped_by_symbol = None

    def process(self) -> PortfolioSummaryModel:
        self.__orderOperationsBySymbol() # esto no es res. de la clase
        portfolio_summary_director = PortfolioSummaryBuilder(self.__operations_grouped_by_symbol)
        portfolio_summary = portfolio_summary_director.process()
        return portfolio_summary

    def __orderOperationsBySymbol(self):
        operations_organizer = OperationsGrouperBySymbol(self.__portfolio.get_operations())
        self.__operations_grouped_by_symbol = operations_organizer.group_operations_by_symbol()