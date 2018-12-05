class QuoteService:
    def __init__(self, quoteHandler):
        self.quoteHandler = quoteHandler
        self.logCollector = "Log Collector"

    def getQuoteById(self, id):
        return self.quoteHandler.getQuoteById(id)
