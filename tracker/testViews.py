from django.test import TestCase
from unittest.mock import patch, MagicMock
from django.urls import reverse
from tracker.external_crypto_price_fetcher import ExternalCryptoPriceFetcher
from tracker.portfolio.symbol_summary_builder import SymbolSummaryBuilder

class PortfolioEndpointTests(TestCase):
    fixtures = ['basicCryptosWithTransactions.json']


    @patch('tracker.external_crypto_price_fetcher.ExternalCryptoPriceFetcher.getPrice')
    def test_portfolio_endpoint(self, mock_get_price):
        mock_prices = {
            'BTC': 101189.11,
            'ETH': 3897.85,
            'BNB': 730.69,
            'NEXO': 1.51,
        }
            
        mock_get_price.side_effect = lambda symbol: mock_prices.get(symbol, 0)

        response = self.client.get(reverse('wallet_api'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        dataKeys = data['data']

        self.assertEqual(dataKeys['ETH']['holdings'], 1.9217)
        self.assertEqual(dataKeys['ETH']['symbol_market_price'], 3897.85)
        self.assertEqual(dataKeys['ETH']['total_cost'], 6955.79)
        self.assertEqual(dataKeys['ETH']['holdings_value'], 7490.5)
        self.assertEqual(dataKeys['ETH']['current_balance'], 534.71)

        self.assertEqual(dataKeys['BTC']['holdings'], 0.0742)
        self.assertEqual(dataKeys['BTC']['symbol_market_price'], 101189.11)
        self.assertEqual(dataKeys['BTC']['total_cost'], 7135.37)
        self.assertEqual(dataKeys['BTC']['holdings_value'], 7508.23)
        self.assertEqual(dataKeys['BTC']['current_balance'], 372.86)

        self.assertEqual(dataKeys['BNB']['holdings'], 2.29)
        self.assertEqual(dataKeys['BNB']['symbol_market_price'], 730.69)
        self.assertEqual(dataKeys['BNB']['total_cost'], 1494.23)
        self.assertEqual(dataKeys['BNB']['holdings_value'], 1673.28)
        self.assertEqual(dataKeys['BNB']['current_balance'], 179.05)

        self.assertEqual(dataKeys['NEXO']['holdings'], 773.13)
        self.assertEqual(dataKeys['NEXO']['symbol_market_price'], 1.51)
        self.assertEqual(dataKeys['NEXO']['total_cost'], 1060.57)
        self.assertEqual(dataKeys['NEXO']['holdings_value'], 1167.43)
        self.assertEqual(dataKeys['NEXO']['current_balance'], 106.86)

        self.assertEqual(data['total_balance'], 1193.48)
