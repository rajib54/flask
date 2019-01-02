from Abstract import QuoteHandlerAbstract
from Model import Quote


class QuoteHandler(QuoteHandlerAbstract):
    def __init__(self):
        self.logCollector = "Log Collector"

    @classmethod
    def getquotes(self):
        quote1 = Quote()
        quote1.id = 1
        quote1.name = "Quote 1"
        quote1array = quote1.toarray()

        quote2 = Quote()
        quote2.id = 2
        quote2.name = "Quote 2"
        quote2array = quote2.toarray()

        quotes = [quote1array, quote2array]

        payload = {
            "payload": {
                "quote": {
                    "quote": quotes
                }
            }
        }
        return payload

    @classmethod
    def getquotebyid(self, id):
        quote = Quote()
        quote.id = int(id)
        quote.name = "Quote " + id

        payload = {
            "payload": {
                "quote": {
                    "quote": [
                        quote.toarray()
                    ]
                }
            }
        }
        return payload
