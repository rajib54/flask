class QuoteService:
    def __init__(self, quotehandlerinterface):
        self.quotehandlerinterface = quotehandlerinterface
        self.logCollector = "Log Collector"

    def getQuoteById(self, id):
        return self.quotehandlerinterface.getQuoteById(id)
