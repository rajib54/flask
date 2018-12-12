import abc


class QuoteHandlerAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getQuoteById(self, id):
        pass
