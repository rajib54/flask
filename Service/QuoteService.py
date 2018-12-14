class QuoteService:
    def __init__(self, quoteabstracthandler):
        self.quoteabstracthandler = quoteabstracthandler
        self.logCollector = "Log Collector"

    def getquotebyid(self, id):
        return self.quoteabstracthandler.getquotebyid(id)

    def getquotes(self):
        return self.quoteabstracthandler.getquotes()
