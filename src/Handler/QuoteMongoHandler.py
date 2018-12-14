from src.Abstract import QuoteHandlerAbstract


class QuoteMongoHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getQuotes(self):
        return "Get data for through mongo"

    @classmethod
    def getQuoteById(self, id):
        return "Get data for through mongo " + format(id)