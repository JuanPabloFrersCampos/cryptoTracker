import decimal

class WalletOverviewService():
    def process(self, allOperations):
        walletOverview = {}
        for operationsGroupedByCrypto in allOperations:
            if not operationsGroupedByCrypto:
                continue
            amountAvailable = self.getAmountOfAvailableCrypto(operationsGroupedByCrypto)
            mediumCost = self.getMediumCost(operationsGroupedByCrypto)
            walletOverview[operationsGroupedByCrypto[0].symbol] = {
                'amountAvailable': amountAvailable,
                'mediumCost': mediumCost
            }
        return walletOverview

    def getAmountOfAvailableCrypto(self, operationsGroupedByCrypto):
        availableCrypto = decimal.Decimal(0)
        for operation in operationsGroupedByCrypto:
            if operation.isSell:
                availableCrypto -= decimal.Decimal(operation.cryptoQuantity)
            else:
                availableCrypto += decimal.Decimal(operation.cryptoQuantity)
        return availableCrypto

    def getMediumCost(self, operationsGroupedByCrypto):
        totalAmount = decimal.Decimal(0)
        totalCost = decimal.Decimal(0)
        for operation in operationsGroupedByCrypto:
            if not operation.isSell:
                totalAmount += decimal.Decimal(operation.cryptoQuantity)
                totalCost += decimal.Decimal(operation.cryptoQuantity) * decimal.Decimal(operation.price)
        if totalAmount == 0:
            return decimal.Decimal(0)
        return totalCost / totalAmount
