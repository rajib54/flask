from Abstract import QuoteHandlerAbstract


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getQuoteById(self, id):
        return "Get data for " + format(id)
