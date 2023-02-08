from abc import abstractmethod, ABCMeta


class MerchantProcessor(metaclass=ABCMeta):
    ERROR_INSUFFICIENT_FUNDS = 'Fondos insuficientes'

    @abstractmethod
    def debit(self):
        pass

class MerchantProcessorDummy(MerchantProcessor):
    def debit(self):
        pass


class MerchantProcessorInsufficientFunds(MerchantProcessor):
    def debit(self):
        raise Exception(self.ERROR_INSUFFICIENT_FUNDS)


class MerchantProcessorSuccess(MerchantProcessor):

    def debit(self):
        return 1
