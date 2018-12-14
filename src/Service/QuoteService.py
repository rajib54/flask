class QuoteService:
    def __init__(self, quoteabstracthandler):
        self.quoteabstracthandler = quoteabstracthandler
        self.logCollector = "Log Collector"

    def getQuoteById(self, id):
        return self.quoteabstracthandler.getQuoteById(id)

    def getQuotes(self):
        return self.quoteabstracthandler.getQuotes()
