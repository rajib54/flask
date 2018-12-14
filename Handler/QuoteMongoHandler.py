from Abstract import QuoteHandlerAbstract


class QuoteMongoHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getquotes(self):
        return "Get data for through mongo"

    @classmethod
    def getquotebyid(self, id):
        return "Get data for through mongo " + format(id)
