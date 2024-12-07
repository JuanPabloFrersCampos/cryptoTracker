from models import PortfolioModel

class PortfolioVisualizer():
    def __init__(self, portfolio: PortfolioModel):
        self.portfolio = portfolio

    def getOperationSetBalances(self):
        