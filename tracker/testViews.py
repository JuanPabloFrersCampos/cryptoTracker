from django.test import TestCase
from .walletOverviewService import WalletOverviewService
from unittest.mock import patch
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

        self.assertEqual(data['ETH']['holdings'], 1.9217)
        self.assertEqual(data['ETH']['symbolMarketPrice'], 3897.85)
        self.assertEqual(data['ETH']['totalCost'], 6955.79)
        self.assertEqual(data['ETH']['holdingsValue'], 7490.69)
        self.assertEqual(data['ETH']['currentBalance'], 534.9)

        self.assertEqual(data['BNB']['holdings'], 2.29)
        self.assertEqual(data['BNB']['symbolMarketPrice'], 730.69)
        self.assertEqual(data['BNB']['totalCost'], 1494.23)
        self.assertEqual(data['BNB']['holdingsValue'], 1673.28)
        self.assertEqual(data['BNB']['currentBalance'], 179.06)

        self.assertEqual(data['BTC']['holdings'], 0.0742)
        self.assertEqual(data['BTC']['symbolMarketPrice'], 101189.11)
        self.assertEqual(data['BTC']['totalCost'], 7135.37)
        self.assertEqual(data['BTC']['holdingsValue'], 7508.23)
        self.assertEqual(data['BTC']['currentBalance'], 372.86)

        self.assertEqual(data['NEXO']['holdings'], 773.13)
        self.assertEqual(data['NEXO']['symbolMarketPrice'], 1.51)
        self.assertEqual(data['NEXO']['totalCost'], 1060.57)
        self.assertEqual(data['NEXO']['holdingsValue'], 1167.43)
        self.assertEqual(data['NEXO']['currentBalance'], 106.86)

        self.assertEqual(data['totalBalance'], 1193.68)
