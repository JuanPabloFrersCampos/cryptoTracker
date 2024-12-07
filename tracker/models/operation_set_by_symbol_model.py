class OperationSetBySymbolModel:
    def __init__(self):
        self.__holdings = None
        self.__symbol_market_price = None
        self.__total_cost = None
        self.__holdings_value = None
        self.__current_balance = None

    def get_holdings(self):
        return self.__holdings

    def set_holdings(self, value):
        self.__holdings = value

    def get_symbol_market_price(self):
        return self.__symbol_market_price

    def set_symbol_market_price(self, value):
        self.__symbol_market_price = value

    def get_total_cost(self):
        return self.__total_cost

    def set_total_cost(self, value):
        self.__total_cost = value

    def get_holdings_value(self):
        return self.__holdings_value

    def set_holdings_value(self, value):
        self.__holdings_value = value

    def get_current_balance(self):
        return self.__current_balance

    def set_current_balance(self, value):
        self.__current_balance = value