from django.test import TestCase
from tracker.portfolio.symbol_summary_builder import SymbolSummaryBuilder
from tracker.externalCryptoPriceFetcher import ExternalCryptoPriceFetcher
from unittest.mock import patch, MagicMock
from django.urls import reverse

class WalletApiViewTests(TestCase):
    fixtures = ['basicCryptosWithTransactions.json']

    @patch.object(WalletOverviewService, 'getSymbolMarketPrice')
    def test_wallet_overview_api(self, walletOverviewServiceMock_getSymbolMarketPrice):
        walletOverviewServiceMock_getSymbolMarketPrice.side_effect = lambda symbol: {
            'BTC': 101189.11,
            'ETH': 3897.85,
            'BNB': 730.69,
            'NEXO': 1.51
        }[symbol.symbol]

        response = self.client.get(reverse('wallet_api'))
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(['ETH']['holdings'], 1.9217)
        self.assertEqual(['ETH']['symbol_market_price'], 4000.5)
        self.assertEqual(['ETH']['total_cost'], 6955.79)
        self.assertEqual(['ETH']['holdings_value'], 7687.45)
        self.assertEqual(['ETH']['current_balance'], 730.66)

        self.assertEqual(['BTC']['holdings'], 0.0742)
        self.assertEqual(['BTC']['symbol_market_price'], 100027.29)
        self.assertEqual(['BTC']['total_cost'], 7135.37)
        self.assertEqual(['BTC']['holdings_value'], 7422.02)
        self.assertEqual(['BTC']['current_balance'], 286.65)

        self.assertEqual(['BNB']['holdings'], 2.29)
        self.assertEqual(['BNB']['symbol_market_price'], 741.89)
        self.assertEqual(['BNB']['total_cost'], 1494.23)
        self.assertEqual(['BNB']['holdings_value'], 1698.93)
        self.assertEqual(['BNB']['current_balance'], 204.7)

        self.assertEqual(['NEXO']['holdings'], 773.13)
        self.assertEqual(['NEXO']['symbol_market_price'], 1.52)
        self.assertEqual(['NEXO']['total_cost'], 1060.57)
        self.assertEqual(['NEXO']['holdings_value'], 1175.16)
        self.assertEqual(['NEXO']['current_balance'], 114.59)

        self.assertEqual(data['total_balance'], 1336.6)
