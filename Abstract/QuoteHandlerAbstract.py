import abc


class QuoteHandlerAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getquotes(self):
        pass

    @abc.abstractmethod
    def getquotebyid(self, id):
        pass
