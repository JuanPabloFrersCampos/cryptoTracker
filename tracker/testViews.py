from django.test import TestCase
from unittest.mock import patch, MagicMock
from django.urls import reverse
from tracker.externalCryptoPriceFetcher import ExternalCryptoPriceFetcher
from tracker.portfolio.symbol_summary_builder import SymbolSummaryBuilder

class PortfolioEndpointTests(TestCase):
    fixtures = ['basicCryptosWithTransactions.json']


    @patch.object(SymbolSummaryBuilder, '_SymbolSummaryBuilder__set_symbol_market_price')
    def test_portfolio_endpoint(self, mock_set_symbol_market_price):
        # Mock getPrice to return specific values based on the symbol
        def mock_method(self, symbol):
            prices = {
                'BTC': 101189.11,
                'ETH': 3897.85,
                'BNB': 730.69,
                'NEXO': 1.51,
            }
            
            # Set the mock price based on the symbol
            self._SymbolSummaryBuilder__symbol_market_price = prices.get(symbol, 0)
            self._SymbolSummaryBuilder__symbol_summary_model.set_symbol_market_price(
                self._SymbolSummaryBuilder__symbol_market_price
            )

        mock_set_symbol_market_price.side_effect = mock_method

        response = self.client.get(reverse('wallet_api'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        dataKeys = data['data']

        self.assertEqual(dataKeys['ETH']['holdings'], 1.9217)
        self.assertEqual(dataKeys['ETH']['symbol_market_price'], 3897.85)
        self.assertEqual(dataKeys['ETH']['total_cost'], 6955.79)
        self.assertEqual(dataKeys['ETH']['holdings_value'], 7687.45)
        self.assertEqual(dataKeys['ETH']['current_balance'], 730.66)

        self.assertEqual(dataKeys['BTC']['holdings'], 0.0742)
        self.assertEqual(dataKeys['BTC']['symbol_market_price'], 100027.29)
        self.assertEqual(dataKeys['BTC']['total_cost'], 7135.37)
        self.assertEqual(dataKeys['BTC']['holdings_value'], 7422.02)
        self.assertEqual(dataKeys['BTC']['current_balance'], 286.65)

        self.assertEqual(dataKeys['BNB']['holdings'], 2.29)
        self.assertEqual(dataKeys['BNB']['symbol_market_price'], 741.89)
        self.assertEqual(dataKeys['BNB']['total_cost'], 1494.23)
        self.assertEqual(dataKeys['BNB']['holdings_value'], 1698.93)
        self.assertEqual(dataKeys['BNB']['current_balance'], 204.7)

        self.assertEqual(dataKeys['NEXO']['holdings'], 773.13)
        self.assertEqual(dataKeys['NEXO']['symbol_market_price'], 1.52)
        self.assertEqual(dataKeys['NEXO']['total_cost'], 1060.57)
        self.assertEqual(dataKeys['NEXO']['holdings_value'], 1175.16)
        self.assertEqual(dataKeys['NEXO']['current_balance'], 114.59)

        self.assertEqual(data['total_balance'], 1336.6)
